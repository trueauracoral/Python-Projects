import requests
import json
import os
import subprocess
import re
import tempfile
import platform

url = "https://invidio.xamh.de/channel/UCo8bcnLyZH8tBIH9V1mLgqQ"
downloader = "yt-dlp"
lbrynet = "lbrynet"
temp_dir = tempfile.TemporaryDirectory().name

url = url.split("/")
if "channel" in url:
    # This is stupid reliance on the piped API because I can't figure
    # out how to get the newest video information from a channel url
    # using yt-dlp directly.
    pipedapi = f"https://pipedapi.kavin.rocks/channel/{url[4]}"
    data = requests.get(pipedapi)
    json_stuff = json.loads(data.text)
    id = str(json_stuff["relatedStreams"][0]["url"]).replace("/watch?v=","")
else:
    id = url[4]
video_data = subprocess.getoutput(f"{downloader} --get-title --get-description --get-thumbnail https://youtube.com/watch?v={id}")
video_data = video_data.splitlines()
title = video_data[0]
thumbnail_url = video_data[1].replace("hqdefault","maxresdefault")
thumbnail_data = requests.get(thumbnail_url)
with open(temp_dir, 'wb') as f:
    f.write(thumbnail_data.content)
description = video_data[2:]
description = '\n'.join(description)
name_thumb = re.sub(r'[\W_]+','', str(title)) + str(123)
name = re.sub(r'[\W_]+','', str(title))

if subprocess.getoutput(f"{lbrynet} version") == "Could not connect to daemon. Are you sure it's running?":
    print('It looks like lbrynet has not started yet. In another terminal window/tab do "lbrynet start" and rerun this script.')
    quit()

channels = subprocess.getoutput(f"{lbrynet} channel list")
json_stuff = json.loads(channels)
for i, channel in enumerate(json_stuff["items"]):
   print(i, "|", channel["name"])

c = 100000
while not c >= 0 or not c <= i:
    c = input('Select a channel from 0-'+str(i)+': ')
    try:
            c = int(c)
    except:
            c = 100000
channel = json_stuff["items"][c]["name"]
print(f"Uploading to {channel}.")
try:
    print("---\nCould be costly to do a upload, press enter and bid will be 0.1")
    bid = str(input("Per upload, how much bid do you want? "))
except:
    bid = str(0.1)

description = (f"""---
This is a LBRY mirror of of this video:
{title}
Original YT URL (THIS IS SPYWARE): https://youtube.com/watch?v={id}
---
{description}""")

print(description)
description = description.replace("\n","\\n")
description = description.replace('"','\\"')
description = description.replace("'","\\'")

print("\n---\nYT download starting:")
os.system(f"{downloader} https://youtube.com/watch?v={id}")

print("\n---\nUploading thumbnail to LBRY!")
thumbnail_command = f'{lbrynet} publish --name={name_thumb} --bid={bid} --file_path="{temp_dir}" --title="{title}" --description="{description}"'
#os.system(thumbnail_command)
thumbnail_data = subprocess.getoutput(thumbnail_command)
json_stuff = json.loads(thumbnail_data)
thumbnail_url = json_stuff["outputs"][0]["permanent_url"].replace("lbry:/","https://spee.ch")
print(thumbnail_url)

if platform.system() == "Windows":
    slash = "\\"
else:
    slash = "/"
cwd = os.getcwd()

print("\n---\nUploading video to LBRY!\n---")
command = f'{lbrynet} publish --name={name} --bid={bid} --file_path="{cwd}{slash}{title} [{id}].mp4" --title="{title}" --description="{description}" --channel_name={channel} --thumbnail="{thumbnail_url}"'
os.system(command)

print("\n---\nLINK:\n---")
print(f"https://spee.ch/{channel}/{name}")
