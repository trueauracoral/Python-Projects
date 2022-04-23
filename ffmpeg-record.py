import os

try:
    output = input("Where do you want the recording to go: ")
    if platform.system() == "Windows":
        os.system(f"ffmpeg -f gdigrab -framerate 30 -i desktop {output}")
    else:
        os.system(f"ffmpeg -f x11grab -i :0.0 -f alsa -i hw:0 {output}")
except:
    quit()
