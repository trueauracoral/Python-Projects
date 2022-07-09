#!/usr/bin/env python
import subprocess
import os
import platform
import requests

player = "mpv"
fzf = "fzf --reverse < FILE"
streams = f"""
anthonywritescode
theprimeagen
rwxrob
tsoding
whitevault
vimlark
mortmort
"""

live_streams = []
with open("streams.txt","w") as f:
    for stream in streams.splitlines():
        # Very cool hack to not use twitch API
        if stream != "" and 'isLiveBroadcast' in requests.get("https://www.twitch.tv/"+stream).content.decode('utf-8'):
            live_streams.append(f"{stream} (Currently LIVE)")
    f.write('\n'.join(live_streams))

choice = subprocess.getoutput(fzf.replace("FILE","streams.txt"))

if choice != "":
    subprocess.Popen(f"{player} https://twitch.tv/{choice}")
os.remove("streams.txt")
