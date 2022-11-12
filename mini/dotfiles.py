#!/usr/bin/env python
import subprocess
import os
import platform
import shutil

def main():
    if platform.system() == "Windows":
        appdata = os.getenv('APPDATA')
        localappdata = os.getenv('LOCALAPPDATA')
    configs = f"""
alacritty - {appdata}\\alacritty\\alacritty.yml
emacs - {appdata}\\.emacs.d\\init.el
mpv - {appdata}\\mpv\\mpv.conf
qutebrowser - {appdata}\\qutebrowser\\config\\config.py
lf - {localappdata}\\lf\\lfrc
wezterm - C:\\SGZ_Pro\\z-Apps_Drivers\\wezterm\\wezterm.lua
bash - C:\\Users\\Stanl\\.bashrc
"""

    git_repo = "C:\SGZ_Pro\Hobbys\coding-projects\Dots\\"
    worked = []
    for config in configs.splitlines():
        if config == "":
            continue
        config = config.split(" - ")
        oldpath = config[1]
        newpath = os.path.join(git_repo, config[0], os.path.basename(oldpath))
        if not os.path.exists(os.path.dirname(newpath)):
            os.mkdir(os.path.dirname(newpath))

        with open(oldpath, "r", encoding="utf-8") as f:
            oldpathtext = f.read()
        with open(newpath, "r", encoding="utf-8") as f:
            newpathtext = f.read()

        if oldpathtext != newpathtext:
            print("OLD: "+oldpath)
            print("NEW: "+newpath)
            shutil.copy(oldpath,newpath)
            worked.append(newpath)

    if len(worked) == 0:
        print("No dotfile updates were found.")
    else:
        print(f"{len(worked)} configs were updated")

if __name__ == "__main__":
    main()
