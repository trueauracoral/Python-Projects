#!/usr/bin/env python
import requests
import os
import sys
import json

downloader = "aria2c"
apiurl = "https://popcorn-time.ga"

def main():
    title = ' '.join(sys.argv[1:]).replace(" ","%20")
    imdbid = json.loads(requests.get(f"https://v2.sg.media-imdb.com/suggests/{title[0]}/{title}.json").text.replace(f"imdb${title.replace('%20','_')}(","").replace(")",""))["d"][0]["id"]
    magnet = requests.get(f"{apiurl}/movie/{imdbid}").json()
    magnet = magnet["torrents"][magnet["original_language"]]["720p"]["url"]
    os.system(f"{downloader} {magnet}")

if __name__ == "__main__":
    main()
