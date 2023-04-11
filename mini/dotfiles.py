#!/usr/bin/env python
import subprocess
import os
import platform
import shutil

def main():
    if platform.system() == "Windows":
        appdata = os.getenv('APPDATA')
        localappdata = os.getenv('LOCALAPPDATA')
    configs = [
        {
            "name": "alacritty",
            "path": f"{appdata}\\alacritty\\alacritty.yml"
        },
        {
            "name": "emacs",
            "path": f"{appdata}\\.emacs.d\\init.el"
        },
        {
            "name": "mpv",
            "path": f"{appdata}\\mpv\\mpv.conf"
        },
        {
            "name": "qutebrowser",
            "path": f"{appdata}\\qutebrowser\\config\\config.py"
        },
        {
            "name": "lf",
            "path": f"{localappdata}\\lf\\lfrc"
        },
        {
            "name": "wezterm",
            "path": f"C:\\SGZ_Pro\\z-Apps_Drivers\\wezterm\\wezterm.lua"
        },
        {
            "name": "bash",
            "path": f"C:\\Users\\Stanl\\.bashrc"
        }
    ]

    git_repo = "C:\SGZ_Pro\Hobbys\coding-projects\Dots\\"
    worked = []
    for config in configs:
        oldpath = config["path"]
        newpath = os.path.join(git_repo, config["name"], os.path.basename(oldpath))
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
