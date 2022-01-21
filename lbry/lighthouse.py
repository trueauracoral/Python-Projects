# Imports
import requests
import json
import os

# Coloring
bold="\033[01m"
norm="\033[00m"
bright_cyan="\033[45m"

# Variables
query = input("Searching for: ")
query = str(query)
size = str(30)
search = 'https://lighthouse.lbry.com/search?s=' + query + '&include=channel,title&size=' + size
# Make sure to have a ending "/"
lbry = "https://lbry.ix.tc/"
# Any command that you can run on your system with the url link.
command = "start "

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
c = 100000
while not c >= 0 or not c <= 29:
    c = input('Number from 1-' + size + " of the URL you want to open: ")
    try:
            c = int(c)
    except:
            c = 100000
selected_url = json_stuff[c]

# Do stuff with it.
url = str(lbry + selected_url["channel"] + "/" + selected_url["name"])
os.system(command + url)
