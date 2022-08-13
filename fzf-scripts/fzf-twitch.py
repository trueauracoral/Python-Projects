#!/usr/bin/env python
import subprocess
import os
import platform
import requests
import sys
from datetime import datetime, timezone
import time
import json
import re

# Streamlink cuts out the add break. But you can just set this to a
# video player such as "mpv".
player = "streamlink --player=mpv --default-stream=best"
fzf = "fzf --reverse < FILE"
streams = f"""anthonywritescode
theprimeagen
rwxrob
tsoding
vimlark
whitevault
mortmort"""
sep = " | "
auth = json.loads(re.findall("streamWeaselsVars = (.*)", requests.get("https://www.streamweasels.com/tools/convert-twitch-username-to-user-id/").text)[0])
headers = {
    "Authorization": f"Bearer {auth['token']}",
    "Client-Id": auth["clientID"]
}
def upcoming(channel):
    date = ""
    info = requests.get(f"https://api.twitch.tv/helix/users?login={channel}", headers=headers).json()
    channel_id = info["data"][0]["id"]
    url = f"https://api.twitch.tv/helix/schedule?broadcaster_id={channel_id}"
    schedule = requests.get(url, headers=headers).json()
    if "error" not in schedule:
        date = datetime.strptime(schedule["data"]["segments"][0]["start_time"], "%Y-%m-%dT%H:%M:%SZ")
        date = date.replace(tzinfo=timezone.utc).astimezone(tz=None)
        abrev_tz = time.tzname[1]
        if " " in abrev_tz:
            abrev_tz = ''.join([x[0] for x in abrev_tz.split(" ")])
        date = date.strftime("%A at %I:%M %p ")+abrev_tz
    return date

def live(channel):
    info = requests.get(f"https://api.twitch.tv/helix/streams?user_login={channel}",headers=headers).json()
    info = info["data"][0]
    return f'{info["user_name"]}{sep}{info["game_name"]}{sep}{info["title"][:50]}{sep}{info["viewer_count"]}'

def main():
    live_streams = []
    upcoming_streams = []
    with open("streams.txt","w",encoding="utf-8") as f:
        for stream in streams.splitlines():
            date = upcoming(stream)
            if stream == "":
                pass
            elif 'isLiveBroadcast' in requests.get("https://www.twitch.tv/"+stream).content.decode('utf-8'):
                live_streams.append(live(stream))
            elif date != "":
                upcoming_streams.append(f"[X] {stream} The next stream is on {date}")
        if live_streams == []:
            live_streams.append("No live streams right now. Below are upcoming:")
        f.write('\n'.join(live_streams+["---"]+upcoming_streams))

    choice = subprocess.getoutput(fzf.replace("FILE","streams.txt"))

    if choice != "":
        subprocess.Popen(f"{player} https://twitch.tv/{choice.split(sep)[0]}")
    elif choice.startswith(("[X]", "---", "No live streams right now")):
        sys.exit(0)
    os.remove("streams.txt")
if __name__ == "__main__":
    main()
