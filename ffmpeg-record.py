import os

try:
    output = input("Where do you want the recording to go: ")
    os.system(f"ffmpeg -f gdigrab -framerate 30 -i desktop {output}")
except:
    quit()
