#!/usr/bin/env python
import requests
import re
import platform
import os

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:17.0) Gecko/20121201 icecat/17.0.1'}
dir = "C:\\SGZ_Pro\\Hobbys\\Media\\pokemon\\"

gens = ["https://projectpokemon.org/home/docs/spriteindex_148/3d-models-generation-1-pok%C3%A9mon-r90/","https://projectpokemon.org/home/docs/spriteindex_148/3d-models-generation-2-pok%C3%A9mon-r91/","https://projectpokemon.org/home/docs/spriteindex_148/3d-models-generation-3-pok%C3%A9mon-r92/","https://projectpokemon.org/home/docs/spriteindex_148/3d-models-generation-4-pok%C3%A9mon-r93/","https://projectpokemon.org/home/docs/spriteindex_148/3d-models-generation-5-pok%C3%A9mon-r94/","https://projectpokemon.org/home/docs/spriteindex_148/3d-models-generation-6-pok%C3%A9mon-r95/","https://projectpokemon.org/home/docs/spriteindex_148/3d-models-generation-7-pok%C3%A9mon-r96/","https://projectpokemon.org/home/docs/spriteindex_148/3d-models-generation-8-pok%C3%A9mon-r123/"]
if platform.system() == "Windows":
    slash = "\\"
else:
    slash = "/"

num2 = 0
for gen in gens:
    num2=num2+1
    os.mkdir(dir+str(num2))
    data = str(requests.get(gen, headers=headers).content)
    links = re.findall("<img alt=.+?>",data)
    num = 0
    for i,link in enumerate(links):
        if "shiny-back" in link:
            pass
        elif "normal-back" in link:
            pass
        elif "shiny-sprite" in link:
            pass
        else:
            num=num+1
            quotes = re.findall('".+?"',link)
            filename = quotes[0].replace('"',"")
            if filename == " ":
                filename = quotes[1].split("/")[-1].replace('"',"")
            print(filename)
            url = quotes[1].replace('"',"")
            print(num, quotes[1].replace("\"",""))
            print(dir+str(num2)+slash+filename)
            with open(dir+str(num2)+slash+filename,"wb") as f:
                f.write(requests.get(url).content)