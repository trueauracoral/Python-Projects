#!/usr/bin/env python

# Script for Pokemon News RSS in rssguard
# Post processing using this API:
# https://www.pokemon.com/api/1/us/news/get-news.json
import re
import json
from datetime import datetime
import requests

URL = "https://www.pokemon.com/api/1/us/news/get-news.json"
json_data = json.loads(requests.get(URL).text)

items = []

for rel in json_data:
  id = rel["url"]
  url = rel["url"]
  title = rel["alt"]
  date = datetime.strptime(rel["date"], "%B %d, %Y").isoformat()
  image = rel["image"]
  html = f"""
<img src='https://www.pokemon.com{image}'>
<p>{rel['shortDescription']}</p>
"""
  item = {
    "author": {"name": "Pokemon Company"},
    "title": title,
    "id": id,
    "content_html": html,
    "url": f"https://pokemon.com{url}",
    "date_published": date
  }
  items.append(item)
json_feed = {
  "title": "Pokemon News",
  "items": items,
}
print(json.dumps(json_feed))
