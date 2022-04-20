# TODO:
# - Config file
#   - Select a main directory
# - Based on season picked create a folder for it (thumbnail needs to match)
# - Select individual video to download
# - Get 9 more seasons of pokemon data

import re
import os
import os.path
from pokeflix_data import *

website = "https://www.pokeflix.tv"
downloader = "yt-dlp"
folder = "C:\\SGZ_Pro\\Hobbys\\Media\\pokemon\\black-white\\"

series = series.splitlines()
for i, gen in enumerate(series):
    if gen.startswith("Generation "):
        print(gen)
genpick = input("Generation number: ")
if genpick.isalpha():
    print("Has to be a number fom 1-8")
    quit()
else:
    for i, serie in enumerate(series):
        if serie.startswith("("+genpick+")"):
            genserie = serie.replace("("+genpick+") ","")
            print(genserie)
            genserieindex = series.index(serie)+1
seriepick = input("Series number: ")
num = genserieindex-int(seriepick)
final = series[num].replace('('+genpick+') ','')
print(f"Picking: {final.replace('Pokemon: ','')}")
final = final.replace("Pokemon: ","").replace(" & ","_").replace(" ","_")

if final in locals():
    videos = globals()[final]
    videos = videos.splitlines()
else:
    print("This season isn't in the database yet...")
    quit()
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
