import requests
import re
import tempfile
import os
import sys

image_viewer = "palemoon"
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:17.0) Gecko/20121201 icecat/17.0.1'}

query = ""
try:
    query = sys.argv[1]
except:
    while not query:
        query = input("Searching for: ")

search = f"https://wiby.me/?q={query}"
search_result = requests.get(search, headers=headers)
search_data = str(search_result.content)

links = re.findall('<a class="tlink" href=.+?>.+?</a>',search_data)
if "submitting a page." in search_data:
    print("Nothing found :(")
    quit()

for i, link in enumerate(links):
    url = re.findall(r'(https?://\S+)', link)
    url = url[0].split('"')[0]
    title = re.sub("<a class=\"tlink\" href=\".+?\">","",link)
    title = title.replace("</a>","").replace("&#39;","'").replace("&amp;","&")
    print(i, title+"\n"+url)
    if i == 10:
        break
