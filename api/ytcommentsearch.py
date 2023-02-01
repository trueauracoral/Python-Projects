#!/usr/bin/env python
import requests
import re
import sys
import argparse

REFERER = "https://ytcomment.kmcat.uk/"

def parse_arguments():
    parser = argparse.ArgumentParser(description='YT comment searcher')
    parser.add_argument('-v', '--video', type=str, metavar='YTVIDEOID', help='A youtube video ID')
    parser.add_argument('-s', '--search', type=str, metavar='Search string', help='Search term for the comment section')
    #parser.add_argument('-li', '--list-instances', action="store_true", default=False, help='List boards')
    return parser.parse_args()

def request(url, jsonify=False):
    r = requests.get(url)
    if not r.ok:
        sys.exit(f"Could not connect to {url}")
    if jsonify == False:
        return r.text
    elif jsonify == True:
        return r.json()

def getKey():
    # THIS WILL BREAK IN THE VERY NEAR FUTURE
    data = request("https://ytcomment.kmcat.uk")
    jsfile = re.findall('<script type="module" src="(.*?)">', data)[0]
    data = request(f"https://ytcomment.kmcat.uk{jsfile[1:]}")
    apiKey = re.findall('apiKey:"(.*?)"', data)[0]
    return apiKey

def commentSearchApi(videoId, searchTerm, apiKey):
    r = requests.get(f"https://www.googleapis.com/youtube/v3/commentThreads?part=id,snippet&videoId={videoId}&pageToken=&order=Relevance&maxResults=100&searchTerms={searchTerm}&textFormat=plainText&key={apiKey}", headers={'referer': REFERER})
    if r.ok:
        return r.json()
    else:
        sys.exit("Could not get comment search api")

def idCheck(videoId, apiKey):
    r = requests.get(f"https://www.googleapis.com/youtube/v3/videos?part=snippet&id={videoId}&key={apiKey}", headers={'referer': REFERER})
    if r.ok:
        r = r.json()
        if len(r["items"]) == 0:
            return False
        else:
            return True
    else:
        sys.exit("Could not get video api")

def main():
    args = parse_arguments()
    apiKey = getKey()

    if idCheck(args.video, apiKey) == True and args.search != "":
        data = commentSearchApi("LkM0Rjvcdhk", args.search, apiKey)["items"]
        for item in data:
            item = item["snippet"]["topLevelComment"]["snippet"]
            print(f"""---
Author: {item['authorDisplayName']}
{item['textDisplay']}
""")
    else:
        sys.exit("Please read the -h/--help")

if __name__ == "__main__":
    main()
