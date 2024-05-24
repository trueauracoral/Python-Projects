#!/usr/bin/env python

# This is broken lol
# Script for Generating RSS from YT community tab
# Example URL: https://www.youtube.com/@PaPaSea/community
import re
import json
from datetime import datetime
from bs4 import BeautifulSoup
import requests
import sys

#sys.stdin.reconfigure(encoding="utf-8")
#
#input_data = sys.stdin.read()

HEADERS = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:17.0) Gecko/20121201 icecat/17.0.1', "Content-Type": "text/html;charset=UTF-8"}
data = requests.get("https://www.pokemon.com/us/pokemon-news", headers=HEADERS).text

#soup = BeautifulSoup(input_data, "html.parser")
soup = BeautifulSoup(data, "html.parser")
name = json.loads(soup.find_all("script")[-6].text.split("var ytInitialData = ")[1].split(";")[-2])
#print(json.dumps(name))
posts = name["contents"]["twoColumnBrowseResultsRenderer"]["tabs"][5]["tabRenderer"]["content"]["sectionListRenderer"]["contents"][0]["itemSectionRenderer"]["contents"]
for post in posts:
    post = post["backstagePostThreadRenderer"]["post"]["backstagePostRenderer"]["contentText"]

items = []

json_feed = {
  "title": "Youtube Community",
  "items": items,
}
print(json.dumps(json_feed))
