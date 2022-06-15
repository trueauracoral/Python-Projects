#!/usr/bin/env python
import requests
import os
import base64

subreddit="entitledparents"
# Some speech to text tool. Output has to be a .wav 
texttospeech = 'mimic -t "TEXT" -o FILE'

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:17.0) Gecko/20121201 icecat/17.0.1'}
data = requests.get(f"https://www.reddit.com/r/{subreddit}.json?limit=400",headers=headers).json()

num = 0
for i, post in enumerate(data["data"]["children"]):
    if i == 0:
        pass
    elif i == 5:
        break
    else:
        num = num+1
        text = post["data"]["selftext_html"].replace(";","")\
                                    .replace("&","")\
                                    .replace("lt","")\
                                    .replace("/div","")\
                                    .replace("!-- SC_ON --","")\
                                    .replace("!-- SC ON --","")\
                                    .replace("!-- SC_OFF --","")\
                                    .replace("!-- SC OFF --","")\
                                    .replace("gt","")\
                                    .replace("div class=\"md\"","")\
                                    .replace("/p","")\
                                    .replace("\n","")\
                                    .replace("amp#39","")
        text = text.encode("ascii","ignore").decode()
        print(text)
        #os.system(texttospeech.replace("TEXT",text).replace("FILE",str(i)+".wav"))

os.system(texttospeech.replace("TEXT",text).replace("FILE","audio.wav"))
text = text.replace(".","").split(" ")
for i, word in enumerate(text):
    print(i)
    imagedata = requests.get(f"https://search.davidovski.xyz/api.php?q={word}&p=1&type=1").json()[0]["base64"]
    os.system(f'ffmpeg -i "data:image/gif;base64,{imagedata}=" {str(i)}.png')
#    decodedata = base64.b64decode(imagedata)
#    try:
#        with open(str(i)+".jpeg","wb") as f:
#            f.write(decodedata)
#    except:
#        print("idk didn't work here")

os.system(f'ffmpeg -y -framerate 1/0.3 -i %d.jpeg -r 25 -vf "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:-1:-1:color=black" -pix_fmt yuv422p input.mp4')
os.system(f'ffmpeg -y -i input.mp4 -i audio.wav output.mp4')

for file in os.listdir():
    if file.endswith(".jpeg"):
        os.remove(file)
os.remove("input.mp4")
