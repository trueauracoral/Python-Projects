import requests
import os

audio = "C:\\SGZ_Pro\\Hobbys\\Media\\music\\lukrembo - butter (royalty free vlog music) [Ua7Qfc1xu90].mp3"
subreddit="pepethefrog"

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:17.0) Gecko/20121201 icecat/17.0.1'}
data = requests.get(f"https://www.reddit.com/r/{subreddit}.json?limit=400",headers=headers).json()

name = 0
format = ".png"
for image in data["data"]["children"]:
    url = image["data"]["url"]
    if url.startswith("https://i.redd.it/"):
        if image["data"]["thumbnail"] == "nsfw":
            pass
        elif url.endswith(format):
            name=name+1
            print(name)
            with open(str(name)+format,"wb") as f:
                f.write(requests.get(image["data"]["url"]).content)
        elif url.endswith(".jpg") or url.endswith(".jpeg"):
            name=name+1
            extension = "."+url.split("/")[3].split(".")[1]
            print(name)
            with open(str(name)+extension,"wb") as f:
                f.write(requests.get(image["data"]["url"]).content)
            os.system(f"ffmpeg -i {name}{extension} -preset ultrafast {name}{format}")

os.system(f'ffmpeg -y -framerate 1 -i %d{format} -vf "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:-1:-1:color=black" -acodec copy input.mp4')
os.system(f'ffmpeg -y -i input.mp4 -i "{audio}" -filter_complex \" [1:0] apad \" -shortest output.mp4')

for file in os.listdir():
    if file.endswith(".png"):
        os.remove(file)
    elif file.endswith(".jpg"):
        os.remove(file)
    elif file.endswith(".jpeg"):
        os.remove(file)
os.remove("input.mp4")
