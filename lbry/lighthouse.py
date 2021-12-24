# Imports
import requests
import json

# Coloring
bold="\033[01m"
norm="\033[00m"
bright_cyan="\033[45m"

# Search stuff
query = input("Searching for: ")
search = 'https://lighthouse.lbry.com/search?s=' + query + '&include=channel,title,thumbnail_url'
data = requests.get(search)
json_stuff = json.loads(data.text)

# Results
for x in json_stuff:
    pre = "lbry://"
    if x["channel"]:
        pre += x["channel"] + "/"
    url = pre + x["name"]
    print(bright_cyan+url+norm)
