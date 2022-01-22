# Imports
import requests
import json
import os

# Coloring
bold="\033[01m"
norm="\033[00m"
bright_cyan="\033[46m"
colora="\033[45m"
colorb="\033[44m"

# Variables
query = input("Searching for: ")
query = str(query)
size = str(19)
search = "https://sepiasearch.org/api/v1/search/videos?search=" + query
# Any command that you can run on your system with the url link.
command = "start "

data = requests.get(search)
json_stuff = json.loads(data.text)
for i, vid in enumerate(json_stuff["data"]):
    print(i, colora+vid["name"]+norm+"\n"+colorb+vid["channel"]["displayName"]+norm+"\n"+bright_cyan+vid["url"]+norm)

# Choose a result
c = 100000
while not c >= 0 or not c <= 19:
    c = input('Number from 1-' + size + " of the URL you want to open: ")
    try:
            c = int(c)
    except:
            c = 100000

selected_url = json_stuff["data"][c]["url"]

# Do stuff with it.
os.system(command + selected_url)
