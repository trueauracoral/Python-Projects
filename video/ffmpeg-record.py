#!/usr/bin/env python
# This is a wrapper script for ffmpeg to do various usefule things.
# Read the help in order to understand in order to close it go to the
# terminal window and press q on your keyboard. If you don't do this
# there is some chance ffmpeg could mess with your recording.
#
# WARNING no gaurentee all these commands work on windows and linux
# because I did not test. And most of these commands I got right off
# of stack exchange and they add crazy options.
import os
import subprocess
import re
import sys
import platform
import argparse

parser = argparse.ArgumentParser(description='Fffmpeg wrapper script.')
parser.add_argument('-s', '--screen', action="store_true", default=False, help='Record screen')
parser.add_argument('-sa', '--screen_audio', action="store_true", default=False, help='Record screen and audio')
parser.add_argument('-a', '--audio', action="store_true", default=False, help='Record just audio')
args = parser.parse_args()

if args.screen:
    output = input("Where do you want the recording to go: ")
    print(platform.system())
    if platform.system() == "Windows":
        os.system(f"ffmpeg -f gdigrab -framerate 30 -i desktop {output}")
    else:
        os.system(f"ffmpeg -f x11grab -i :0.0 -f alsa -i hw:0 {output}")
elif args.audio:
    devices = subprocess.getoutput("ffmpeg -list_devices true -f dshow -i dummy")
    data = re.findall('"(.+?)"',devices)
    for i,device in enumerate(data):
        print(i, device)
    pick = data[int(input("Which audio device do you want? "))]
    if pick.startswith("@"):
        pick = data[data.index(pick)-1]
    output = input("Where do you want the recording to go: ")
    command = f'ffmpeg -f dshow -i audio="{pick}" {output}'
    try:
        os.system(command)
    except:
        quit()
elif args.screen_audio:
    devices = subprocess.getoutput("ffmpeg -list_devices true -f dshow -i dummy")
    data = re.findall('"(.+?)"',devices)
    for i,device in enumerate(data):
        print(i, device)
    pick = data[int(input("Which audio device do you want? "))]
    if pick.startswith("@"):
        pick = data[data.index(pick)-1]
    output = input("Where do you want the recording to go: ")
    # On windows this command is supposed to work for getting screen
    # resolution "wmic desktopmonitor get screenheight, screenwidth"
    # but for me it doesn't work. In the future when linux support is
    # added xrandr could be used to get screen resolution and select
    # which monitor to use etc. But for now ffmpeg is basicly geussing
    # stuff.
    command = f'ffmpeg -f gdigrab -framerate ntsc -i desktop -f dshow -i audio="{pick}" -vcodec libx264 -pix_fmt yuv420p -preset ultrafast {output}'
    os.system(command)

# Add an overlay thing on the lower right corner of the video
# ffmpeg -i whole.mp4 -i meme.png -filter_complex "[0:v][1:v] overlay=W-w:H-h" -pix_fmt yuv420p -c:a copy wholeimage.mp4
