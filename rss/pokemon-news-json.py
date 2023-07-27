#!/usr/bin/env python

# Script for Pokemon News RSS in rssguard
# Post processing using this API:
# https://www.pokemon.com/api/1/us/news/get-news.json
import re
import json
import sys
from datetime import datetime

sys.stdin.reconfigure(encoding="utf-8")

input_data = sys.stdin.read()
json_data = json.loads(input_data)

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
    "url": url,
    "date_published": date
  }
  items.append(item)
json_feed = {
  "title": "Pokemon News",
  "items": items,
}
print(json.dumps(json_feed))
