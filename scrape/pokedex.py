import requests
import re
import sys
import tempfile
import random
import os

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:17.0) Gecko/20121201 icecat/17.0.1'}
image_viewer = "palemoon"
temp_dir = tempfile.TemporaryDirectory().name

query = ""
try:
    query = sys.argv[1]
except:
    while not query:
        query = input("Searching for: ")

search = f"https://pokemondb.net/pokedex/{query}"
search_result = requests.get(search, headers=headers)
search_data = str(search_result.content)
pokedex = re.findall('<td class="cell-med-text">(.+?)</td>',search_data)

try:
    print(pokedex[random.randint(0,len(pokedex))])
except:
    print("ERROR: Either you mispelled or this pokemon doesn't exist")

try:
    image = re.findall('<img src=(.+?)>',search_data)
    url = re.findall(r'(https?://\S+)', image[0].replace("\"",""))
    print(url[0])
    thumbnail_data = requests.get(url[0])
    with open(temp_dir, 'wb') as f:
        f.write(thumbnail_data.content)
    os.system(f"{image_viewer} {temp_dir}")
except:
    print("ERROR: Could not get image")
