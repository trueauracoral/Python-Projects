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
#query = "trueauracoral"
query = str(query)
size = str(30)
search = 'https://lighthouse.lbry.com/search?s=' + query + '&include=channel,title&size=' + size
lbry = "https://lbry.ix.tc/"
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
channel_ID = json_stuff[0]["claimId"]
claim_ID = selected_url["claimId"]
channel_name = json_stuff[0]["name"]
url = str(lbry + "api/comments?claim_id=" + claim_ID + "&channel_id=" + claim_ID + "&channel_name=" + channel_name + "&page=1&page_size=15")

comments = requests.get(url)
json_comments = json.loads(comments.text)
for i, x in enumerate(json_comments["comments"]):
    print(i, bright_cyan+x["Channel"]["Name"]+norm+"\n"+x["Comment"])
