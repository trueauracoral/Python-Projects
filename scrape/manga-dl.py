#!/usr/bin/env python

#RECOURCES: 
#https://github.com/tsihoarana/manga-scraper/blob/master/scrap.py
#https://www.howtolovecomics.com/2019/05/07/pokemon-manga-guide/

# HOW TO:
# I was kinda lazy, time limited, and probably won't use this script
# many times in the future. Use the `-v` flag and input a manga4life URL
import requests
from bs4 import BeautifulSoup
import json
from PIL import Image
import os
import argparse 

def get_arguments():
    parser = argparse.ArgumentParser(description='Manga DL')
    parser.add_argument('-v', '--volume', type=str, metavar='VOLUME', help='select which volumes you want')
    #parser.add_argument('-g', '--general', action="store_true", default=False, help='Get general emotes')
    args = parser.parse_args()
    return args

def get_volumes(url):
    title = url.split("/")[-2]
    data = requests.get(url).text
    soup = BeautifulSoup(data, "html.parser")
    chapters = json.loads(str(soup.find_all("script")[-1]).split("vm.Chapters = ")[1].split(";")[0])
    num = len(chapters)
    volumes = []
    for i in list(range(1, num+1)):
        volumes.append(f"https://manga4life.com/read-online/{title}-chapter-{i}-page-1.html")
    return volumes

def get_pages(url):
    data = requests.get(url).text
    soup = BeautifulSoup(data, "html.parser")
    data = soup.find_all("script")[-1]
    title = str(data).split("vm.IndexName = \"")[1].split("\";")[0]
    chapters = json.loads(str(data).split("vm.CHAPTERS = ")[1].split(";")[0])
    pages = int(chapters[0]['Page'])
    chapter = url.split(".html")[0].split("-")[-1]
    urls = []
    for i in list(range(1, pages+1)):
        urls.append(f"https://official-ongoing-1.ivalice.us/manga/{title}/{chapter.zfill(4)}-{str(i).zfill(3)}.png")
    return urls

def make_pdf(urls):
    images = []
    files = []
    total = len(urls)
    vol = urls[0].split("/")[-1].split("-")[0]
    for i, url in enumerate(urls):
        filename = url.split("/")[-1]
        title = url.split("/")[-2]
        data = requests.get(url)
        if not os.path.isfile(filename):
            with open(filename, "wb") as f:
                f.write(data.content)
        files.append(filename)
        images.append(Image.open(url.split("/")[-1]))
        print(f"{url} ({i}/{total})")
    images[0].save(title+"-Volume"+vol+".pdf", "PDF", resolution=100.0, save_all=True, append_images=images)
    for file in files:
        os.remove(file)

def fzf(data):
    p = subprocess.run(COMMAND, input=data, capture_output=True, text=True)
    if p.stdout == "":
        sys.exit("Please select something.")
    else:
        return int(p.stdout.split("\n")[0].split(":")[0]) - 1

def main():
    args = get_arguments()
    if args.volume:
        volumes = get_volumes(args.volume)
        title = args.volume.split("/")[-1]
        total = len(volumes)
        selection = input(f"Select which volumes to download: 1-{total}: ").split("-")
        start = int(selection[0])
        end = int(selection[1])
        for volume in list(range(start, end+1)):
            make_pdf(get_pages(f"https://manga4life.com/read-online/{title}-chapter-{volume}.html"))
            print(f"Finished downloading volume {volume}")
    #make_pdf(get_pages("https://manga4life.com/read-online/Pocket-Monster-Special-chapter-1.html"))

if __name__ == '__main__':
    main()
