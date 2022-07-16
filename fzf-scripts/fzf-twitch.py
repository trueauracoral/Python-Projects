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
streams = f"""anthonywritescode
theprimeagen
rwxrob
tsoding
vimlark
whitevault
mortmort"""

# I got this from streamweasels.com under network in the f12
headers = {
    "Authorization": "Bearer oll661c5pnlw0txizn436sbqxuig6q",
    "Client-Id": "os2kmdts5tvcojd34pguyzsn3eyn5q"
}
def upcoming(channel):
    date = ""
    info = requests.get(f"https://api.twitch.tv/helix/users?login={channel}", headers=headers).json()
    channel_id = info["data"][0]["id"]
    url = f"https://api.twitch.tv/helix/schedule?broadcaster_id={channel_id}"
    schedule = requests.get(url, headers=headers).json()
    if "error" not in schedule:
        date = datetime.strptime(schedule["data"]["segments"][0]["start_time"], "%Y-%m-%dT%H:%M:%SZ")
        # Thank you Cringe, Doctor Tiberius Cringe
        date = date.replace(tzinfo=timezone.utc).astimezone(tz=None)
        abrev_tz = time.tzname[1]
        if " " in abrev_tz:
            abrev_tz = ''.join([x[0] for x in abrev_tz.split(" ")])
        date = date.strftime("%A at %I:%M %p ")+abrev_tz
    return date

def live(channel):
    info = requests.get(f"https://api.twitch.tv/helix/streams?user_login={channel}",headers=headers).json()
    info = info["data"][0]
    return f'{info["user_name"]} | {info["game_name"]} | {info["title"][:50]} | {info["viewer_count"]}'

def main():
    live_streams = []
    upcoming_streams = []
    with open("streams.txt","w") as f:
        for stream in streams.splitlines():
            date = upcoming(stream)
            if stream == "":
                pass
            elif 'isLiveBroadcast' in requests.get("https://www.twitch.tv/"+stream).content.decode('utf-8'):
                live_streams.append(live(stream))
            elif date != "":
                upcoming_streams.append(f"{stream} The next stream is on {date}")
        if live_streams == []:
            live_streams.append("No live streams right now. Below are upcoming:")
        f.write('\n'.join(live_streams+["---"]+upcoming_streams))
    
    choice = subprocess.getoutput(fzf.replace("FILE","streams.txt"))
    
    if choice != "":
        subprocess.Popen(f"{player} https://twitch.tv/{choice}")
    elif "The next stream" in choice:
        sys.exit(0)
    os.remove("streams.txt")
if __name__ == "__main__":
    main()
