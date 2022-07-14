#!/usr/bin/env python
import subprocess
import os
import platform
import requests
import sys
from datetime import datetime, timezone

player = "mpv"
fzf = "fzf --reverse < FILE"
streams = f"""
anthonywritescode
theprimeagen
rwxrob
tsoding
vimlark
whitevault
mortmort
"""

def main():
    # I got this from streamweasels.com under network in the f12
    headers = {
        "Authorization": "Bearer oll661c5pnlw0txizn436sbqxuig6q",
        "Client-Id": "os2kmdts5tvcojd34pguyzsn3eyn5q"
        }
    channel_id = requests.get("https://api.twitch.tv/helix/users?login=whitevault", headers=headers).json()["data"][0]["id"]
    url = f"https://api.twitch.tv/helix/schedule?broadcaster_id={channel_id}"
    schedule = requests.get(url, headers=headers).json()
    if "error" not in schedule:
        date = datetime.strptime(schedule["data"]["segments"][0]["start_time"], "%Y-%m-%dT%H:%M:%SZ")
        # Thank you Cringe, Doctor Tiberius Cringe
        corrected = date.replace(tzinfo=timezone.utc).astimezone(tz=None).strftime("%A at %I:%M %p %z")
        print(corrected)
        print(type(date))
    #live_streams = []
    #with open("streams.txt","w") as f:
    #    for stream in streams.splitlines():
    #        # Very cool hack to not use twitch API
    #        if stream != "" and 'isLiveBroadcast' in requests.get("https://www.twitch.tv/"+stream).content.decode('utf-8'):
    #            live_streams.append(f"{stream} (Currently LIVE)")
    #    f.write('\n'.join(live_streams))
    #
    #if live_streams == []:
    #    print("None of your followed streams are lived currently :(")
    #    sys.exit(1)
    #choice = subprocess.getoutput(fzf.replace("FILE","streams.txt"))
    #
    #if choice != "":
    #    subprocess.Popen(f"{player} https://twitch.tv/{choice}")
    #os.remove("streams.txt")
if __name__ == "__main__":
    main()
