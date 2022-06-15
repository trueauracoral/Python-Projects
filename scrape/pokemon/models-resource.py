#!/usr/bin/env python
import requests
from zipfile import ZipFile
import platform
import re
import os

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:17.0) Gecko/20121201 icecat/17.0.1'}
if platform.system() == "Windows":
    slash = "\\"
else:
    slash = "/"

url = "https://www.models-resource.com/3ds/pokemonxy"
domain = url.split("/")[2]

data = str(requests.get(url, headers=headers).content)
links = re.findall('<a href=".+?" style="text-decoration',data)
for i,link in enumerate(links):
    quotes = re.findall('".+?"',link)
    link = "https://"+domain+quotes[0].replace('"',"")
    if "vg-resource" in link:
        pass
    else:
        print(link)
        data = str(requests.get(link,headers=headers).content).replace("\n","")
        name = re.findall('<li>.+?</li>',data)[0].split("/")[1].lower()
        print(name)
        download = "https://"+domain+re.findall('<a href=".+?" style="text',data)[2].replace('<a href="',"").replace('" style="text',"")
        print(download)
        with open(name+".zip","wb") as f:
            f.write(requests.get(download).content)
        with ZipFile(name+".zip","r") as zip:
            zip.extractall()
        os.rename("Pokemon XY",name)
        os.remove(name+".zip")