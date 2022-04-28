import os
import subprocess
import re

#try:
#    output = input("Where do you want the recording to go: ")
#    if platform.system() == "Windows":
#        os.system(f"ffmpeg -f gdigrab -framerate 30 -i desktop {output}")
#    else:
#        os.system(f"ffmpeg -f x11grab -i :0.0 -f alsa -i hw:0 {output}")
#except:
#    quit()

devices = subprocess.getoutput("ffmpeg -list_devices true -f dshow -i dummy")
devices = re.findall('"(.+?)"',devices)
for i,device in enumerate(devices):
    if device.startswith("@"):
        pass
    else:
        print(i, device)
# Record Audio
# ffmpeg -f dshow -i audio="Microphone (USB Audio Device)" output.mp3

# Record video
# ffmpeg -f gdigrab -framerate 30 -i desktop output.mp4
# ffmpeg -f gdigrab -framerate ntsc -video_size 1920x1080 -i desktop  -f dshow -i audio="Microphone (Realtek High Definition Audio)" -vcodec libx264 -pix_fmt yuv420p -preset ultrafast D:\Movies\output.mp4
