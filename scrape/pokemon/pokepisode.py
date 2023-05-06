#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup
import json

def request(url, jsonify=False):
    r = requests.get(url)
    if not r.ok:
        sys.exit("Could not request url")

    if jsonify == False:
        return r.text
    elif jsonify == True:
        return r.json()

def gogoanime():
    gogoanime = request("https://ww5.gogoanimes.org/ajaxajax/load-list-episode?ep_start=0&ep_end=&id=0&default_ep=&alias=/category/pokemon-shinsaku-anime")
    soup = BeautifulSoup(gogoanime, 'html.parser')
    newest = soup.find_all("li")[0]
    number = int(newest.find('div', attrs={'class':'name'}).text.split(" ")[-1])
    link = "https://ww5.gogoanimes.org"+newest.find('a')['href'][1:]
    return {
        "link": link,
        "number": number
    }

def tvmaze():
    data = request(f"https://api.tvmaze.com/search/shows?q=pokemon", jsonify=True)
    data = request(data[0]["show"]["_links"]["self"]["href"], jsonify=True)
    previousepisode = request(data["_links"]["previousepisode"]["href"], jsonify=True)
    return {
        "name": previousepisode["name"],
        "number": previousepisode["number"],
    }

def somestuffs():
    data = request(f"https://some-stuffs.com/")
    soup = BeautifulSoup(data, 'html.parser')
    newest = soup.find("script", attrs={'id':'__NEXT_DATA__'}).text
    content = json.loads(newest)["props"]["pageProps"]["allPosts"]
    details = [(episode) for episode in content if episode["categories"][0] == "pokemon"][0]
    number = int(details["slug"].split("-")[-1])
    soup = BeautifulSoup(details["mdContent"], 'html.parser')
    url = soup.find("a")['href']
    torrent = url.replace("view", "download")+".torrent"
    return {
        "torrent": torrent,
        "url": url,
        "number": number
    }

def main():
    official = tvmaze()
    print(f"""Newest released episode is {official['number']} - {official['name']}""")

    clear = gogoanime()
    print(f"""GOGOanime has released episode {clear['number']}
- LINK: {clear['link']}""")

    tor = somestuffs()
    print(f"""Tor has released episode {tor['number']}
- LINK:\t\t{tor['url']}
- Torrent:\t{tor['torrent']}""")

if __name__ == "__main__":
    main()
