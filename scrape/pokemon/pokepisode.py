#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup
import json
import argparse
import sys
from datetime import datetime
import re

# This changes almost every week
# Of the many problems in this code, this is the biggest. I must
# scrape this crap
GOGOANIME = "anitaku.to"

def parse_arguments():

    parser = argparse.ArgumentParser(description='Check to See when new Pokemon Episodes drop')

    #parser.add_argument('link', type=str, metavar='URL', help='IMDB link')
    parser.add_argument('-g', '--gogoanime', action="store_true", default=False, help='Get gogoanime link')
    parser.add_argument('-t', '--torrent', action="store_true", default=False, help='Get nyaa.si torrent link')

    args = parser.parse_args()

    return args

def request(url, jsonify=False):
    r = requests.get(url)
    if not r.ok:
        sys.exit("Could not request url")

    if jsonify == False:
        return r.text
    elif jsonify == True:
        return r.json()

def gogoanime():
    gogoanime = request("https://ajax.gogo-load.com/ajax/load-list-episode?ep_start=0&ep_end=100000000&id=13784&default_ep=0&alias=pokemon-shinsaku-anime")
    soup = BeautifulSoup(gogoanime, 'html.parser')
    newest = soup.find_all("li")[0]
    number = int(newest.find('div', attrs={'class':'name'}).text.split(" ")[-1])
    link = f"https://{GOGOANIME}"+newest.find('a')['href'][1:]
    return {
        "link": link,
        "number": number
    }

def wikipedia():
    data = request("https://en.wikipedia.org/w/index.php?title=Pok%C3%A9mon_Horizons:_The_Series&useskin=vector")
    soup = BeautifulSoup(data, 'html.parser')
    table = soup.find("table", {"class": "wikitable plainrowheaders wikiepisodetable"})
    rows = table.find_all("tr")
    current_date = datetime.now()
    last_episode = {}
    next_episode = {}

    def title_format(title):
        return re.findall('".*?"', title)[0]
    for i, row in enumerate(rows):
        columns = row.find_all("td")
        if len(columns) > 1:
            date_string = columns[6].text.strip().split("(")[-1].replace(")","")
            episode_date = datetime.strptime(date_string, "%Y-%m-%d")
            if episode_date <= current_date:
                last_episode = {
                    "number": columns[1].text.strip(),
                    "title": title_format(columns[2].text.strip()),
                    "date": date_string
                }
            else:
                next_episode = {
                    "number": columns[1].text.strip(),
                    "title": title_format(columns[2].text.strip()),
                    "date": date_string
                }
                break
    return (last_episode, next_episode)

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
    args = parse_arguments()

    if args.gogoanime:
        print(gogoanime()["link"])
    elif args.torrent:
        print(somestuffs()["url"])
    else:
        # Not sure how tvmaze gets it's data from. Now on I will just
        # scrape wikipedia
        # official = tvmaze()
        wiki = wikipedia()
        released = wiki[0]
        next_episode = wiki[1]
        print(f"""Newest released episode is {released['number']} - {released['title']}""")

        clear = gogoanime()
        print(f"""
GOGOanime has released episode {clear['number']}
- LINK: {clear['link']}""")

        tor = somestuffs()
        print(f"""
Tor has released episode {tor['number']}
- LINK:\t\t{tor['url']}
- Torrent:\t{tor['torrent']}""")

        if len(wiki[1]) != 0:
            print(f"""\nNext episode is {next_episode['number']} - {next_episode['title']} on {next_episode['date']}""")
        else:
            print("Not sure when the next episode is unfortunately. Check back soon!")

if __name__ == "__main__":
    main()
