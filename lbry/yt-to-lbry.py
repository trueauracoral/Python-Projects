# ISSUES:
# - keeps \n, \" and \' in description.
# - You need to put a pipedapi.kavin.rocks url for it to work.
import requests
import json
import os
import subprocess
import re
import tempfile
import platform

url = "https://pipedapi.kavin.rocks/channel/UCu17Sme-KE87ca9OTzP0p7g"
downloader = "yt-dlp"
lbrynet = "lbrynet"
temp_dir = tempfile.TemporaryDirectory().name

data = requests.get(url)
json_stuff = json.loads(data.text)
id = str(json_stuff["relatedStreams"][0]["url"]).replace("/watch?v=","")
video = requests.get("https://pipedapi.kavin.rocks/streams/"+id)
video_json = json.loads(video.text)
title = video_json["title"]
name_thumb = re.sub(r'[\W_]+','', str(title)) + str(123)
name = re.sub(r'[\W_]+','', str(title))

if subprocess.getoutput(f"{lbrynet} stop") == "Could not connect to daemon. Are you sure it's running?":
    print('It looks like lbrynet has not started yet. In another terminal window/tab do "lbrynet start" and rerun this script.')
    quit()

channels = subprocess.getoutput(f"{lbrynet} channel list")
json_stuff = json.loads(channels)
for i, channel in enumerate(json_stuff["items"]):
   print(i+1, "|", channel["name"])

c = 100000
while not c >= 0 or not c <= i:
    c = input('Select a channel from 1-'+str(i)+': ')
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
{video_json["description"]}""")

print(description)
description = description.replace("\n","\\n")
description = description.replace('"','\\"')
description = description.replace("'","\\'")

print("\n---\nYT download starting:")
os.system(f"{downloader} https://youtube.com/watch?v={id}")

print("\n---\nUploading thumbnail to LBRY!")
thumbnail_data = requests.get(video_json["thumbnailUrl"])
with open(temp_dir, 'wb') as f:
    f.write(thumbnail_data.content)

thumbnail_command = f'{lbrynet} publish --name={name_thumb} --bid={bid} --file_path="{temp_dir}" --title="{title}" --description="{description}" --channel_name={channel}'
os.system(thumbnail_command)

if platform.system() == "Windows":
    slash = "\\"
else:
    slash = "/"
cwd = os.getcwd()

command = f'{lbrynet} publish --name={name} --bid={bid} --file_path="{cwd}{slash}{title} [{id}].mp4" --title="{title}" --description="{description}" --channel_name={channel} --thumbnail="https://spee.ch/{channel}/{name_thumb}"'
os.system(command)

print("\nLINK:")
print(f"https://spee.ch/{channel}/{name}")
