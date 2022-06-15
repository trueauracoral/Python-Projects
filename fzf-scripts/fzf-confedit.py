#!/usr/bin/env python
import subprocess
import os
import platform

editor = "emacs"
fzf = "fzf --reverse < FILE"

if platform.system() == "Windows":
    appdata = os.getenv('APPDATA')
configs = f"""
alacritty - {appdata}\\alacritty\\alacritty.yml
emacs - {appdata}\\.emacs.d\\init.el
mpv - {appdata}\\mpv\\mpv.conf
qutebrowser - {appdata}\\qutebrowser\\config\\config.py
"""

with open("configs.txt","w") as f:
    f.write(configs)

choice = subprocess.getoutput(fzf.replace("FILE","configs.txt")).split(" - ")[1]
if choice is not "":
    subprocess.Popen(f"{editor} {choice}")
os.remove("configs.txt")