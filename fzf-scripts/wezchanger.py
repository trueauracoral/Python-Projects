#!/usr/bin/env python
import json
import re
import requests
import subprocess
import os

CONFIG = "C:\\SGZ_Pro\\Z-Apps_drivers\\wezterm\\wezterm.lua"
FZF = "fzf --reverse < FILE"

def main():
    data = requests.get("https://raw.githubusercontent.com/wez/wezterm/main/docs/colorschemes/data.json").text
    schemes = re.findall('"name": "(.*)",', data)

    with open("schemes.txt", "w") as f:
        f.write('\n'.join(schemes))

    choice = subprocess.getoutput(FZF.replace("FILE","schemes.txt"))

    if choice != "":
        text = open(CONFIG, "r").read()
        with open(CONFIG, "w") as f:
            new = re.sub("[ \t]color_scheme = \"(.*)", f"\tcolor_scheme = \"{choice}\",", text)
            f.write(new)
    os.remove("schemes.txt")

if __name__ == "__main__":
    main()
