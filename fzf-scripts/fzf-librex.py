#!/usr/bin/env python
import urllib.parse
import urllib.request
import json
import subprocess
import argparse
import tempfile
import os
import re
import random
import sys
# This somehow fixes issues with urllib ssl errors (FOR ME)
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# Set this to False if you want LIBREX_INSTANCE to be used.
RANDOM_INSTANCE = True
# To find more instances go to:
# https://github.com/hnhx/librex/#instances
LIBREX_INSTANCE = "https://search.davidovski.xyz/"
TORRENT = "aria2c"
PLAYER = "mpv"
BROWSER = "palemoon"
IMAGE = "mpv"# You can change this to a normal image viewer

def get_arguments():
    parser = argparse.ArgumentParser(description='fzf-librex')
    parser.add_argument('-s', '--search', type=str, metavar='TEXT', help='Search the internet (text)', nargs='+')
    parser.add_argument('-i', '--image', type=str, metavar='TEXT', help='Search for images', nargs='+')
    parser.add_argument('-t', '--torrent', type=str, metavar='TEXT', help='Search various torrent websites.', nargs='+')
    parser.add_argument('-v', '--video', type=str, metavar='TEXT', help='Search for videos', nargs='+')
    #parser.add_argument('-c', '--copy', action="store_true", default=False, help='Copy the link to the pasted file')
    return parser.parse_args()


def get_random_instance():
    md = str(urllib.request.urlopen("https://raw.githubusercontent.com/hnhx/librex/main/README.md").read())
    links = re.findall("\(.+?\)",md)[:-1]
    working = []
    for link in links:
        link = link.replace(")","").replace("(","")
        if not link.endswith(("onion/","i2p/")):
            if urllib.request.urlopen(link).getcode() == 200:
                working.append(link)
    return random.choice(working)


def api(search_text, search_type):
    search_type = str(search_type)
    search_text = ' '.join(search_text)
    if RANDOM_INSTANCE == False:
        instance = LIBREX_INSTANCE
    elif RANDOM_INSTANCE == True:
        instance = get_random_instance()
        print(f"Using random instance: {instance}")
    search_url = urllib.parse.urljoin(instance,f"/api.php?q={urllib.parse.quote(search_text)}&type={search_type}")
    # Use this line if urllib isn't working for you and you have
    # requests:
    #data = requests.get(search_url).json()
    return json.loads(urllib.request.urlopen(search_url).read())


def fzf(search, type_, opener):
    type_ = str(type_)
    data = api(search, type_)
    file = tempfile.TemporaryFile().name
    sep = " | "
    with open(file,"a",encoding="utf-8") as f:
        for i, result in enumerate(data):
            if type_ == "0" or type_ == "2":
                f.write(f'{i} {result["title"]}{sep}{result["url"]}\n')
            elif type_ == "1":
                f.write(f'{i} {result["alt"]}{sep}{result["url"]}\n')
            elif type_ == "3":
                f.write(f'{i} ({result["source"]}) {result["size"]} [S:{result["leechers"]}, L:{result["seeders"]}] {result["name"]}\n')
    with open(file, "r", encoding="utf-8") as f:
        text = '\n'.join(f.read().splitlines()[:-1])

    choice = subprocess.getoutput(f"fzf --reverse < {file}")
    if choice != "":
        feed = {
            "0": "url",
            "1": "thumbnail",
            "2": "url",
            "3": "magnet",
        }
        num = int(choice.split(" ")[0])
        subprocess.Popen([opener, urllib.parse.unquote(data[num][feed[type_]])])
    os.remove(file)
    

def main():
    args = get_arguments()
    if len(sys.argv) == 1:
        print("No arguments were given. Read the help (-h/--help).")
        sys.exit(1)
    if args.search:
        fzf(args.search, 0, BROWSER)
    elif args.image:
        fzf(args.image, 1, IMAGE)
    elif args.video:
        fzf(args.video, 2, PLAYER)
    elif args.torrent:
        fzf(args.torrent, 3, TORRENT)

if __name__ == "__main__":
    main()