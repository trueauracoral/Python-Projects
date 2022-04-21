# TODO:
# - [ ] Select individual video to download
# - [x] Config file
# - [x] Fix input errors such as putting 0 or number way too big
# - [x] Select a main directory
# - [x] Based on season picked create a folder for it
# - [x] Get 9 more seasons of pokemon data

import re
import os
import os.path
from pokeflix_data import *
from configparser import ConfigParser
config = ConfigParser()
config.read('pokeflix.conf')
website = config.get('CONFIG','website')
downloader = config.get('CONFIG','downloader')
main_folder = config.get('CONFIG','main_folder')

series = series.splitlines()
for i, gen in enumerate(series):
    if gen.startswith("Generation "):
        print(gen)
try:
    genpick = int(input("Generation number: "))
except:
    print("ERROR: Needs to be an ineger")
    quit()
if genpick <= 0 or genpick > 8:
    print("ERROR: Has to be a number fom 1-8")
    quit()
else:
    genpick = str(genpick)
    for i, serie in enumerate(series):
        if serie.startswith("("+genpick+")"):
            genserie = serie.replace("("+genpick+") ","")
            print(genserie)
            genserieindex = series.index(serie)+1
seriepick = int(input("Series number: "))
if seriepick < 0 or seriepick > 4:
    print("ERROR: Has to be number from 1-4")
    quit()
num = genserieindex-seriepick
# needs some mechanism to detect bad input
final = series[num].replace('('+genpick+') ','')
print(f"Picking: {final.replace('Pokemon: ','')}")
final = final.replace("Pokemon: ","").replace(" & ","_").replace(" ","_").replace(":","")

if final in locals():
    videos = globals()[final]
    videos = videos.splitlines()
else:
    print("ERROR: This season isn't in the database yet...")
    quit()
folder = main_folder+final.replace("_","-").lower()+"\\"
print(f"Will be downloading to {folder}")
if os.path.exists(folder):
    pass
else:
    os.mkdir(folder)
yesno = input("Try to get thumbnails needs requests (N/y): ")
if yesno == "yes" or yesno == "Y" or yesno == "y":
    get_thumb = True
else:
    get_thumb = False
if get_thumb == True:
    import requests
    if os.path.exists(folder+"thumbnails"):
        pass
    else:
        os.mkdir(folder+"thumbnails")

for video in videos:
    if video.startswith("/static"):
        if get_thumb == True:
            thumbnail_data = requests.get(website+video)
            name = folder+"thumbnails\\"+video.split("/")[4]
            with open(name,"wb") as f:
                f.write(thumbnail_data.content)
            print("GETTING THUMBNAILS")
    elif video.startswith("/video"):
        os.system(f"cd {folder} && {downloader} {website+video}")
    else:
        print(video)
    
# Only usefule for RAW HTML.
#data = re.findall('<a href="(.+?)">',videos)
#for link in data:
#    link = link.replace("\" class=\"btn btn-default","")
#    print("https://www.pokeflix.tv" + link)
#    os.system(f"cd {folder} && {downloader} https://www.pokeflix.tv{link}")
