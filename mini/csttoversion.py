#!/usr/bin/env python
import os
import requests

# This script is automating the solution posted on
# https://community.citra-emu.org/t/how-can-i-find-the-version-of-my-save-state/334167/9#post_10
# When you do the dumb thing of updating citra while your save states
# expect you to be on the version of citra you saved on. This script
# will find the version of citra you need to make stuff work

VERSION = "nightly"
def main():
    # haha windows lol
    appdata = os.getenv('APPDATA')
    directory = os.path.join(appdata, "citra/states/")
    saves = os.listdir(directory)
    os.chdir(directory)
    for i, save in enumerate(saves):
        print(f"Save #{i+1}")
        with open(save, 'rb') as f:
            hexdata = f.read().hex()
        sha = hexdata[24:64]
        print(f"https://github.com/citra-emu/citra-nightly/commit/{sha}")
        releases = requests.get("https://api.github.com/repos/citra-emu/citra-nightly/releases").json()
        for release in releases:
            if release["target_commitish"] == sha:
                print(release["html_url"])
if __name__ == "__main__":
    main()
