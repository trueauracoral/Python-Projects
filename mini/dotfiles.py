#!/usr/bin/env python
import subprocess
import os
import platform
import shutil
import argparse
import sys
import subprocess
import pyperclip

# Put environment variables that you need for your platform
# I want to add multiplatform support in the future
if platform.system() == "Windows":
    # https://learn.microsoft.com/en-us/windows/deployment/usmt/usmt-recognized-environment-variables
    appdata = os.getenv('APPDATA')
    localappdata = os.getenv('LOCALAPPDATA')
    home = os.getenv('USERPROFILE')


COMMAND = ["fzf", "--reverse", "--delimiter", " | "]
# Put your desired configurator here
EDITOR = "vim"
# Dotfiles destination
git_repo = "C:\\SGZ_Pro\\Hobbys\\coding-projects\\Dots\\"
# This should eventually go into a config file
CONFIGS = [
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
        "name": "neofetch",
        "path": f"{home}\\.config\\neofetch\\config.conf"
    },
    {
        "name": "bash",
        "path": f"{home}\\.bashrc"
    }
]

def get_arguments():
    parser = argparse.ArgumentParser(description='dotfiles.py - If you give this script no arguments then it will just copy the files to a git repo directory you set in the script')
    parser.add_argument('-o', '--open', action="store_true", default=False, help='FZF select which config to open')
    return parser.parse_args()

def copy():
    worked = []
    for config in CONFIGS:
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

def fzf(data):
    p = subprocess.run(COMMAND, input=data, capture_output=True, text=True)
    if p.stdout == "":
        sys.exit("Please select something.")
    else:
        return p.stdout.split(" | ")[1]

def openDots():
    data = ""
    for config in CONFIGS:
        #https://stackoverflow.com/questions/33323715/python-evenly-space-output-data-with-varying-string-lengths
        data += f"{config['name']:15s} | {config['path']}\n"
    path = fzf(data)
    pyperclip.copy(path)
    print(f"copied {path}")
    # idk I am stupid and don't know how to actually open in editor
    #subprocess.Popen([EDITOR, fzf(data)])

def main():
    args = get_arguments()
    if args.open:
        openDots()
    else:
        copy()

if __name__ == "__main__":
    main()
