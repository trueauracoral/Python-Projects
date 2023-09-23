#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup
import json
import argparse
import sys

# This changes almost every week
GOGOANIME = "gogoanimehd.io"

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
        official = tvmaze()
        print(f"""Newest released episode is {official['number']} - {official['name']}""")

        clear = gogoanime()
        print(f"""
GOGOanime has released episode {clear['number']}
- LINK: {clear['link']}""")

        tor = somestuffs()
        print(f"""
Tor has released episode {tor['number']}
- LINK:\t\t{tor['url']}
- Torrent:\t{tor['torrent']}""")

if __name__ == "__main__":
    main()
