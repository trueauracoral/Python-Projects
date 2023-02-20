#!/usr/bin/env python
import requests

shows = [
    "Velma",
    "Pokemon",
    "Wednesday",
    "Oddballs",
]

def request(url, jsonify=False):
    r = requests.get(url)
    if not r.ok:
        sys.exit("Could not request url")

    if jsonify == False:
        return r.text
    elif jsonify == True:
        return r.json()

def main():
    for show in shows:
        data = request(f"https://api.tvmaze.com/search/shows?q={show}", jsonify=True)
        thelinks = data[0]["show"]["_links"]
        if "nextepisode" in thelinks:
            episode = request(thelinks["nextepisode"]["href"], jsonify=True)
            if episode['number'] != None:
                se = f"S{episode['season']}E{episode['number']}"
            else:
                se = f"S{episode['season']}"
            print(f"{show}: Next episode {se} \"{episode['name']}\" airing on {episode['airdate']}")
        else:
            print(f"{show}: Has no upcoming episodes :(")

if __name__ == "__main__":
    main()
