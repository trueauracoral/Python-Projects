# This program gathers data about a YT channel's videos or any YT link
# using yt-dl or yt-dlp and then mirrors it to LBRY. yt-dlp
# theoretticaly can be used to mirror from sites like peertube but it
# probalby won't work as well. So right now, this program tries to
# only accept YT channel links or YT watch links. Most invidious links
# should also work.

# Commands:
# python yt-to-lbry.py <YT CHANNEL URL>
# mirror all of the videos from the channel to LBRY
# WARNING: Takes a while and requires a lot of space depending on the
# size of the channel
#
# python yt-to-lbry.py <YT VIDEO URL>
# mirror the video to LBRY

# in the future make it so you can get just *1* of the new videos
# from a channel
#command = f"{downloader} --get-title --get-description --get-thumbnail --get-id https://youtube.com/channel/{channel_id} --playlist-end 1"
import requests
import sys
import json
import os
import subprocess
import re
import tempfile
import platform
import random
import time

downloader = "yt-dlp"
lbrynet = "lbrynet"
temp_dir = tempfile.TemporaryDirectory().name

if subprocess.getoutput(f"{lbrynet} version") == "Could not connect to daemon. Are you sure it's running?":
    print('It looks like lbrynet has not started yet. In another terminal window/tab do "lbrynet start" and rerun this script.')
    quit()

url = ""
try:
    url = sys.argv[1]
except:
    while not url:
        url = input("YT URL: ")

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

def upload(command):
    video_data = subprocess.getoutput(command)
    video_data = video_data.splitlines()
    title = video_data[0]
    id = video_data[1]
    thumbnail_url = video_data[2]
    thumbnail_data = requests.get(thumbnail_url)
    with open(temp_dir, 'wb') as f:
        f.write(thumbnail_data.content)
    description = video_data[3:]
    description = '\n'.join(description)
    keys = ("abcdefghijklmnopqrxtuvwsyz" + "ABCDEFGHIJKLMNOPQRXTUV" + "1234567890")
    name_thumb = ("".join(random.sample(keys,50)))
    name = re.sub(r'[\W_]+','', str(title))


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
    os.system(f"{downloader} https://youtube.com/watch?v={id} --format=mp4")

    print("\n---\nUploading thumbnail to LBRY!")
    thumbnail_command = f'{lbrynet} publish --name={name_thumb} --bid={bid} --file_path="{temp_dir}" --title="{title}" --description="{description}"'
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

split_url = url.split("/")
if "channel" in url:
    channel_id = split_url[4]
    print("Getting data from the channel. This might take a while...")
    data = subprocess.getoutput(f"{downloader} --get-id https://youtube.com/channel/{channel_id}")
    data = data.splitlines()
    for id in data:
        print(id)
        upload(f"{downloader} --get-title --get-description --get-thumbnail --get-id https://youtube.com/watch?v={id}")
        # Lbrynet might break from a lot of uploading. So got to put a
        # 20 second delay.
        time.sleep(20)

elif "watch" in url:
    id = split_url[3].replace("watch?v=","")
    upload(f"{downloader} --get-title --get-description --get-thumbnail --get-id https://youtube.com/watch?v={id}")
else:
    print("This URL isn't supported yet :(")
    quit()
