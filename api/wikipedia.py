#!/usr/bin/env python
import requests
import json
import os
import sys
import re

bold = "\033[01m"
norm = "\033[00m"
bright_cyan = "\033[46m"
colora = "\033[45m"
colorb = "\033[44m"

search = input("Wikipedia Snippet: ")
wikipedia_api = f"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch={search}&format=json"

data = requests.get(wikipedia_api)
json_stuff = json.loads(data.text)

for index, post in enumerate(json_stuff["query"]["search"]):
        clean = re.compile('<.*?>')
        print(re.sub(clean, '', post["title"]+"\n"+post["snippet"]+"\n"))
        if index == 2:
            break
