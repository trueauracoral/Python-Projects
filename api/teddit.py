import requests
import json
import os
import sys

bold = "\033[01m"
norm = "\033[00m"
bright_cyan = "\033[46m"
colora = "\033[45m"
colorb = "\033[44m"

subreddit = input("Subreddit: ")
teddit_api = "https://teddit.net/r/" + subreddit + "?api&target=reddit"
data = requests.get(teddit_api)
json_stuff = json.loads(data.text)

for i, post in enumerate(json_stuff["links"]):
    if post["selftext_html"] == None:
        print(colora+post["title"]+norm+colorb+"\n"+post["url"]+norm+"\n")
    else:
        print(colora+post["title"]+norm+colorb+"\n"+post["url"]+norm+"\n"+post["selftext_html"])
