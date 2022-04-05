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

search = f"https://tenor.com/search/{query}-gifs"
search_result = requests.get(search, headers=headers)
search_data = str(search_result.content)

links = re.findall('<img src=.+?>',search_data)
if "No Results" in search_data:
    print("Nothing found :(")
    quit()
    
for i, link in enumerate(links[34:]):
    url = re.findall(r'(https?://\S+)', link)
    url = url[0].replace("\"", "")
    print(i, url)
    if i == 10:
        break

    temp_dir = tempfile.TemporaryDirectory().name
    thumbnail_data = requests.get(url)
    with open(temp_dir, 'wb') as f:
        f.write(thumbnail_data.content)
    os.system(image_viewer + " " + temp_dir)
