import requests
import json
import os
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

thumbnail_command = f'{lbrynet} publish --name={name_thumb} --bid=0.1 --file_path="{temp_dir}" --title="{title}" --description="{description}" --channel_name=@TrueAuraCoralPublishesImages'
print(thumbnail_command)
os.system(thumbnail_command)

if platform.system() == "Windows":
    slash = "\\"
else:
    slash = "/"
cwd = os.getcwd()

command = f'{lbrynet} publish --name={name} --bid=0.1 --file_path="{cwd}{slash}{title} [{id}].mp4" --title="{title}" --description="{description}" --channel_name=@TrueAuraCoralPublishesImages --thumbnail="https://spee.ch/@TrueAuraCoralPublishesImages/{name_thumb}"'
print(command)
os.system(command)
