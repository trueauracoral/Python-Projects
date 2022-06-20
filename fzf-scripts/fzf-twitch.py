#!/usr/bin/env python
import subprocess
import os
import platform

player = "mpv"
fzf = "fzf --reverse < FILE"

streams = f"""
theprimeagen
rwxrob
tsoding
"""

with open("streams.txt","w") as f:
    f.write(streams)

choice = subprocess.getoutput(fzf.replace("FILE","streams.txt"))
if choice != "":
    subprocess.Popen(f"{player} https://twitch.tv/{choice}")
os.remove("streams.txt")