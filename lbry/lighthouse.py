# Imports
import requests
import json
import os

browser = 'librewolf.exe'
# Coloring
bold="\033[01m"
norm="\033[00m"
bright_cyan="\033[45m"

# Search stuff
query = input("Searching for: ")
query = str(query)
search = 'https://lighthouse.lbry.com/search?s=' + query + '&include=channel,title'
data = requests.get(search)
json_stuff = json.loads(data.text)

# Results
for i, x in enumerate(json_stuff):
    pre = "lbry://"
    if x["channel"]:
        pre += x["channel"] + "/"
    url = pre + x["name"]
    print(i, bright_cyan+url+norm)

# Choose a result
c = 42
while not c >= 0 or not c <= 9:
    c = input("Number from 1-9 of the URL you want to open: ")
    try:
            c = int(c)
    except:
            c = 42
selected_url = json_stuff[c]

# Do stuff
url = str("https://lbry.ix.tc/" + selected_url["channel"] + "/" + selected_url["name"])
os.system("start " + url)
