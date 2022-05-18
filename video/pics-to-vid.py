import requests
import os

audio = "C:\\SGZ_Pro\\Hobbys\\Media\\music\\lukrembo - butter (royalty free vlog music) [Ua7Qfc1xu90].mp3"
subreddit = "pepethefrog"

#data = requests.get("https://teddit.net/r/unixporn?api&target=reddit").json()
# The benifit of using the reddit API is you can get a lot of images
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:17.0) Gecko/20121201 icecat/17.0.1'}
data = requests.get(f"https://www.reddit.com/r/{subreddit}.json?limit=400",headers=headers).json()

name = 0
for image in data["data"]["children"]:
    if image["data"]["url"].startswith("https://i.redd.it/") and image["data"]["url"].endswith(".png"):
        name=name+1
        print(name)
        with open(str(name)+".png","wb") as f:
            f.write(requests.get(image["data"]["url"]).content)

os.system(f'ffmpeg -y -framerate 1 -i %d.png -vf "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:-1:-1:color=black" -acodec copy input.mp4')
os.system(f'ffmpeg -y -i input.mp4 -i "{audio}" -filter_complex \" [1:0] apad \" -shortest output.mp4')

for file in os.listdir():
    if file.endswith(".png"):
        os.remove(file)
os.remove("input.mp4")
