import json
import requests
import tempfile
import os

key = "LIVDSRZULELA"
image_viewer = "palemoon"
query = ""
try:
    query = sys.argv[1:]
    query = ' '.join(query)
except:
    while not query:
        query = input("Searching for: ")
    query = str(query)
size = str(10)
search = f"https://g.tenor.com/v1/search?q={query}&key={key}&limit={size}"
data = requests.get(search)
json_stuff = json.loads(data.text)

for i, x in enumerate(json_stuff["results"]):
    print(i, x["media"][0]["mediumgif"]["url"])
    temp_dir = tempfile.TemporaryDirectory().name
    thumbnail_data = requests.get(x["media"][0]["mediumgif"]["url"])
    with open(temp_dir, 'wb') as f:
        f.write(thumbnail_data.content)
    os.system(f"{image_viewer} {temp_dir}")

#c = 100000
#while not c >= 0 or not c <= 29:
#    c = input('Number from 1-' + size + " of the URL you want to open: ")
#    try:
#            c = int(c)
#    except:
#            c = 100000
#
#selected_url = json_stuff["results"][c]["media"][0]["mediumgif"]["url"]
#
#print(selected_url)
