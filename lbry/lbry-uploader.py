#!/usr/bin/env python
import random
import string
import json
import os
import subprocess
import re

lbrynet = "lbrynet"
# Got from: https://notabug.org/jyamihud/FastLBRY-terminal/src/master/flbry/variables.py#L502
licenses = [
    # NAME , URL , COMMENT
    ["GNU General Public License Version 3 (or later)",
     "https://www.gnu.org/licenses/gpl-3.0.html",
     "Strong Copyleft. Recommended for Software."],
    ["GNU General Public License Version 3 (only)",
     "https://www.gnu.org/licenses/gpl-3.0.html",
     "Strong Copyleft."],
    ["GNU Free Documentation License",
     "https://www.gnu.org/licenses/fdl-1.3.html",
     "Strong Copyleft. Recommended for books."],
    ["Creative Commons Attribution-ShareAlike 4.0 International",
     "https://creativecommons.org/licenses/by-sa/4.0/",
     "Copylefted, Recommended for Art."],
    ["Creative Commons Attribution 4.0 International",
     "https://creativecommons.org/licenses/by/4.0/",
     "Non Copylefted, Free License."],
    ["Creative Commons Zero 1.0 International",
     "https://creativecommons.org/publicdomain/zero/1.0/",
     "Public Domain"],
    ["Creative Commons Attribution-NoDerivatives 4.0 International",
     "https://creativecommons.org/licenses/by-nd/4.0/",
     "Does not allow changes. Recommended for opinion pieces."]
]

# Check that lbry sdk is running.
if subprocess.getoutput(f"{lbrynet} version") == "Could not connect to daemon. Are you sure it's running?":
    print('It looks like lbrynet has not started yet. In another terminal window/tab do "lbrynet start" and rerun this script.')
    quit()

# Channel
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

print(f"Uploading to {channel}.\n---")

# Title
title = input("Title for the publication: ")

# Url
print("---\nPressing enter will make it the title just with removed special characters.")
name = input("Custome lbry url name: ")
if name == "":
    name = re.sub(r'[\W_]+','', str(title))

# Bid
try:
    print("---\nCould be costly to do a upload, press enter and bid will be 0.1")
    bid = str(input("Per upload, how much bid do you want? "))
except:
    bid = str(0.1)

# Description
try:
    print("---\nPressing enter will make the publication not have a description")
    description = input("Description for publication: ")
    #description = description.replace("\n","\\n")
    description = description.replace('"','\\"')
    description = description.replace("'","\\'")
except:
    description = ""

# Thumbnail
try:
    print("---\nIf you want, a thumbnail can be uploaded to lbry. It will have all atributes of the video just the lbry name will be plus 123. Press enter for no thumbnail.")
    thumbnail = input("Thumbnail file location: ")
except:
    thumbnail = ""
 	
keys = ("abcdefghijklmnopqrxtuvwsyz" + "ABCDEFGHIJKLMNOPQRXTUV" + "1234567890")
name_thumb = ("".join(random.sample(keys,50)))

# Publication
print("---\nFinally we are at the last step!")
publication = input("Publication file location: ")

# License
for i, license in enumerate(licenses):
    print(i,*licenses[i],sep='\n')

l = 100000
while not l >= 0 or not l <= 7:
    l = input('Select a license from 0-7: ')
    try:
            l = int(l)
    except:
            l = 100000

license = licenses[l][0]
license_url = licenses[l][1]


if thumbnail == "":
    print("---\nUploading puplication to LBRY!\n---")
    command = f'{lbrynet} publish --name="{name}" --bid={bid} --file_path="{publication}" --title="{title}" --description="{description}" --channel_name={channel} --license="{license}" --license_url="{license_url}"'
    os.system(command)
else:
    print("\n---\nUploading thumbnail to LBRY!")
    thumbnail_command = f'{lbrynet} publish --name="{name_thumb}" --bid={bid} --file_path="{thumbnail}" --title="{title}" --description="{description}"'
    print(thumbnail_command)
    thumbnail_data = subprocess.getoutput(thumbnail_command)
    json_stuff = json.loads(thumbnail_data)
    thumbnail_url = json_stuff["outputs"][0]["permanent_url"].replace("lbry:/","https://spee.ch")
    print("\n---\nUploading puplication to LBRY!\n---")
    command = f'{lbrynet} publish --name={name} --bid={bid} --file_path="{publication}" --title="{title}" --description="{description}" --channel_name={channel} --thumbnail="{thumbnail_url}" --license="{license}" --license_url="{license_url}"'
    print(command)
    os.system(command)

print("\n---\nLINK:\n---")
print(f"https://spee.ch/{channel}/{name}")
