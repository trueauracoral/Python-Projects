#!/usr/bin/env python

import requests
import sys

def api(id):
    request = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{id}.json?print=pretty")
    if request.status_code != 200:
        sys.exit(f"Could not fetch {id}")
    return request.json()

maxitem = requests.get("https://hacker-news.firebaseio.com/v0/maxitem.json?print=pretty")
if maxitem.status_code != 200:
    sys.exit(f"Could not fetch max id")
maxitem = int(maxitem.text)

hnrange = list(range(1, maxitem))

for post in hnrange:
    print(post)
    data = api(post)
    if data["type"] == "story" and data["dead"] == False:
        print(f"{data['by']} - {data['title']} - {data['url']}")
    elif data["type"] in ["comment", "poll"]:
        print(f"{data['by']} - {data['text']}")
    elif data["type"] == "job":
        print(f"{data['by']} - {data['title']} - {data['text']}")
