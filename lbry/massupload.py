import os
import subprocess
import re
import platform
import time
import sys
import json

lbrynet = "lbrynet"
files = os.listdir()
if platform.system() == "Windows":
    slash = "\\"
else:
    slash = "/"
file_path = os.getcwd() + slash

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
print(f"Mass uploading to {channel}.")

try:
    print("---\nCould be costly to do a mass upload, press enter and bid will be 0.1")
    bid = str(input("Per upload, how much bid do you want? "))
except:
    bid = str(0.1)

#try:
#    print('---\nDo you want a special description? Press enter and the description will be "mass upload"')
#    description = input('Description for every upload: ')
#except:
#    description = "mass upload"

for image in files:
    print(image)
    if image == sys.argv[0]:
        pass
    os.system(f'{lbrynet} publish --name={image} --bid=0.1 --file_path="{file_path + image}" --title="{image}" --channel_name={channel}')
    time.sleep(30)

for image in files:
    print(f"https://spee.ch/{channel}/{image}")
