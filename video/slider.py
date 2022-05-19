import os
import requests
import re

textfile = "slider.txt"
audio = "C:\\SGZ_Pro\\Hobbys\\Media\\music\\lukrembo - butter (royalty free vlog music) [Ua7Qfc1xu90].mp3"

with open(textfile,"r") as f:
    data = f.read()
# This assumes you have stuff in '' not ""
files = re.findall("'(.+?)'",data)

for file in files:
    if file.endswith(".jpg") or file.endswith(".jpeg"):
        beforedot = url.split(".")[0]
        os.system(f"ffmpeg -y -i {file} -preset ultrafast {beforedot}.png")
        os.remove(file)

for file in files:
    if file.endswith(".png"):
        os.system(f'ffmpeg -i {file} -vf "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:-1:-1:color=black" edit-{file}')
        os.remove(file)
        os.rename("edit-"+file,file)

os.system(f"ffmpeg -f concat -i {textfile} -vsync vfr -pix_fmt yuv420p input.mp4")
os.system(f'ffmpeg -y -i input.mp4 -i "{audio}" -filter_complex \" [1:0] apad \" -shortest output.mp4')
os.remove("input.mp4")
