#!/usr/bin/env python
import subprocess
import os
import platform
import shutil

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

for config in configs.splitlines():
    if config == "":
        pass
    else:
        config = config.split(" - ")
        oldpath = config[1]
        newpath = os.path.join(git_repo, config[0], os.path.basename(oldpath))
        if not os.path.exists(os.path.dirname(newpath)):
            os.mkdir(os.path.dirname(newpath))
        print("OLD: "+oldpath)
        print("NEW: "+newpath)
        shutil.copy(oldpath,newpath)
