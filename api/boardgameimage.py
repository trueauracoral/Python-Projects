#!/usr/bin/env python
import requests 
import xml.etree.ElementTree as ET

with open("Board Games.csv", encoding="utf8") as f:
    text = f.read()

links = []
for line in text.splitlines():
    links.append(line.split(",")[-1])
print(links)

working = []
total = len(links)
for num, link in enumerate(links):
    if link == "Image":
        working.append("Image")
        continue
    link = "https://"+link.split("/")[2]+"/xmlapi/"+'/'.join(link.split("/")[3:])
    data = requests.get(link).text
    myroot = ET.fromstring(data)
    for i in myroot.findall('boardgame'):
        image = i.find('image').text
        print(f"{image} ({num}/{total})")
        working.append(image)
print(working)
with open("urls.txt", "w") as f:
    f.write('\n'.join(working))

finaletext = []
for line, image in zip(text.splitlines(), working):
    finaletext.append(line+","+image)

with open("finaleboardgame.csv", "w", encoding="utf8") as f:
    f.write('\n'.join(working))