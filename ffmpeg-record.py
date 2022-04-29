import os
import subprocess
import re
import sys

if len(sys.argv) == 1:
    print("HA LOL")
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

# Audio & Video record
# ffmpeg -f gdigrab -framerate ntsc -video_size 1920x1080 -i desktop  -f dshow -i audio="Microphone (Realtek High Definition Audio)" -vcodec libx264 -pix_fmt yuv420p -preset ultrafast D:\Movies\output.mp4
