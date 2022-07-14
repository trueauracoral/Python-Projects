#!/usr/bin/env python
import subprocess
import os
import platform
import requests
import sys
from datetime import datetime, timezone
import time

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

def upcoming(channel):
    date = ""
    # I got this from streamweasels.com under network in the f12
    headers = {
        "Authorization": "Bearer oll661c5pnlw0txizn436sbqxuig6q",
        "Client-Id": "os2kmdts5tvcojd34pguyzsn3eyn5q"
        }
    info = requests.get(f"https://api.twitch.tv/helix/users?login={channel}", headers=headers).json()
    channel_id = info["data"][0]["id"]
    url = f"https://api.twitch.tv/helix/schedule?broadcaster_id={channel_id}"
    schedule = requests.get(url, headers=headers).json()
    if "error" not in schedule:
        date = datetime.strptime(schedule["data"]["segments"][0]["start_time"], "%Y-%m-%dT%H:%M:%SZ")
        # Thank you Cringe, Doctor Tiberius Cringe
        date = date.replace(tzinfo=timezone.utc).astimezone(tz=None)
        abrev_tz = ''.join([x[0] for x in time.tzname[1].split(" ")])
        date = date.strftime("%A at %I:%M %p ")+abrev_tz
    return date
def main():
    live_streams = []
    with open("streams.txt","w") as f:
        for stream in streams.splitlines():
            if stream == "":
                pass
            elif 'isLiveBroadcast' in requests.get("https://www.twitch.tv/"+stream).content.decode('utf-8'):
                live_streams.append(f"{stream} (Currently LIVE)")
            elif upcoming(stream) != "":
                live_streams.append(f"{stream} The next stream is on {upcoming(stream)}")
        f.write('\n'.join(live_streams))
    
    if live_streams == []:
        print("None of your followed streams are lived currently :(")
        sys.exit(1)
    choice = subprocess.getoutput(fzf.replace("FILE","streams.txt"))
    
    if choice != "":
        subprocess.Popen(f"{player} https://twitch.tv/{choice}")
    elif "The next stream" in choice:
        sys.exit(1)
    os.remove("streams.txt")
if __name__ == "__main__":
    main()
