import requests
import re
import sys
import tempfile
import random
import os

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:17.0) Gecko/20121201 icecat/17.0.1'}
image_viewer = "palemoon"
dir = "C:\\SGZ_Pro\\Hobbys\\Media\\pokemon\\"

database = "https://pokemondb.net/pokedex/national"
request = requests.get(database, headers=headers)
data = str(request.content)

images = re.findall('<span class="img-fixed img-sprite" data-src=".+?>',data)
for i, image in enumerate(images):
    url = re.findall(r'(https?://\S+)', image.replace("\"",""))[0]
    print(url)
    name = re.sub('<span class="img-fixed img-sprite" data-src=".+?" data-alt="',"",image).replace(" sprite\">","").lower()
    if "\\" in name:
        name = name.split("\\")[0]
    print(name)

    thumbnail_data = requests.get(url)
    with open(dir + name + ".png", 'wb') as f:
        f.write(thumbnail_data.content)
