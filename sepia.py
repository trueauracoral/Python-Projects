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
command = "C:\\SGZ_Pro\\z-apps_drivers\\mpv\\mpv.exe "

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
comments = "https://" + json_stuff["data"][c]["account"]["host"] + "/api/v1/videos/" + json_stuff["data"][c]["uuid"] + "/comment-threads"
data_comment = requests.get(comments)
json_comment = json.loads(data_comment.text)
for i, comment in enumerate(json_comment["data"]):
    if comment["account"] == None:
        print(i, "No Account Data")
    else:
        #print(i, comment["account"]["displayName"])
        print(i, colora+comment["account"]["displayName"]+norm+"\n"+colorb+comment["text"]+norm)
os.system(command + selected_url)
