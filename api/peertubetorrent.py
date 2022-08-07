#!/usr/bin/env python
import requests
import sys
import argparse
import os

# If you prefer torrents write "torrent"
type = "magnet"
download = "aria2c"

if len(sys.argv) == 1 or sys.argv[1] == "-h" or sys.argv[1] == "--help":
    print(f"{sys.argv[0]} PEERTUBE_VIDEO_URL QUALITY")
elif len(sys.argv) == 3:
    link = sys.argv[1]
    link = link.split("/w/")
    instance = link[0]
    vidid = link[1]
    quality = sys.argv[2]
    data = requests.get(f"{instance}/api/v1/videos/{vidid}")
    if data.status_code != 200:
        print("Could not find this video.")
        sys.exit(1)
    else:
        data = data.json()

    qualities = []
    for torrent in data["files"]:
        label = torrent["resolution"]["label"]
        qualities.append(label)
    if quality in qualities:
        if type == "torrent":
            link = data['files'][qualities.index(quality)]['torrentDownloadUrl']
            print(f"{label} {link}")
            os.system(f"{download} {link}")
        elif type == "magnet":
            link = data['files'][qualities.index(quality)]['torrentDownloadUrl']
            print(f"{label} {link}")
            os.system(f"{download} {link}")
    else:
        print("Could not find this resolution, try 360p, 480p, 1080p")
        sys.exit(1)
else:
    print("Not enouph arguments, read the help (-h/--help).")
