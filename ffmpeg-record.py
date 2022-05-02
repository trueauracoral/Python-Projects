# This script is windows only right now. When I switch to Linux I will
# try and convert all ffmpeg options to be appropriate for a Linux
# most likely X11 system. I am not an ffmpeg pro, I am just
# researching options and using it over something like OBS for
# things. Hopefully in the future I will put PeerTube livestreaming
# and maybe LBRY if that is possible.
import os
import subprocess
import re
import sys

if len(sys.argv) == 1:
    print("A missing or incorrect option was given")

elif sys.argv[1] == "-s":
    try:
        output = input("Where do you want the recording to go: ")
        if platform.system() == "Windows":
            os.system(f"ffmpeg -f gdigrab -framerate 30 -i desktop {output}")
        else:
            os.system(f"ffmpeg -f x11grab -i :0.0 -f alsa -i hw:0 {output}")
    except:
        quit()

elif sys.argv[1] == "-a":
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

elif sys.argv[1] == "-sa":
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
    try:
        os.system(command)
    except:
        quit()

# Add an overlay thing on the lower right corner of the video
# ffmpeg -i whole.mp4 -i meme.png -filter_complex "[0:v][1:v] overlay=W-w:H-h" -pix_fmt yuv420p -c:a copy wholeimage.mp4
