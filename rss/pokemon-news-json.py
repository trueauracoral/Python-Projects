#!/usr/bin/env python
import re
import json
import sys
from datetime import datetime

input_data = sys.stdin.read()
json_data = json.loads(input_data)

json_feed = "{{\"title\": \"{title}\", \"items\": [{items}]}}"
items = list()

for rel in json_data:
  id = json.dumps(rel["tags"][0]["label"])
  url = json.dumps(rel["url"])
  title = json.dumps(rel["alt"])
  date = json.dumps(datetime.strptime(rel["date"], "%B %d, %Y").isoformat())
  html = json.dumps(rel["shortDescription"])
  items.append(f'{{"author": "Pokemon Company", "title": {title}, "id": {id}, "content_html": {html}, "url": {url}, "date_published": {date}}}')

json_feed = json_feed.format(title = "Pokemon News", items = ", ".join(items))
print(json_feed)
