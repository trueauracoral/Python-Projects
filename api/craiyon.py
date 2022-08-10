#!/usr/bin/env python
import requests
import base64
import sys
from PIL import Image
import os
import subprocess

VIEWER = ["mpv", "--keep-open"]
FORMAT = "jpeg"

def main():
    headers = {
        "authority": "backend.craiyon.com",
        "accept": "application/json",
        "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
        "content-type": "application/json",
        "origin": "https://www.craiyon.com",
        "referer": "https://www.craiyon.com/",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15",
    }

    prompt = ' '.join(sys.argv[1:])
    if prompt == "":
        print(f"Need to give a prompt of what you want to see!\nExample: {sys.argv[0]} A flying pig.")
        sys.exit(1)

    print("This will take some time...")
    data = requests.post("https://backend.craiyon.com/generate", headers=headers, json={"prompt": prompt}).json()

    for i, image in enumerate(data["images"]):
        image = image.replace('"','').replace("\\n","\n")
        decodedata = base64.b64decode(image)
        with open(f"{i+1}.jpeg","wb") as f:
            f.write(decodedata)
    grid = Image.new('RGB', size=(3*256, 3*256))

    grid.paste(Image.open("1.jpeg"), (0, 0))
    grid.paste(Image.open("2.jpeg"), (256, 0))
    grid.paste(Image.open("3.jpeg"), (512, 0))
    grid.paste(Image.open("4.jpeg"), (0, 256))
    grid.paste(Image.open("5.jpeg"), (256, 256))
    grid.paste(Image.open("6.jpeg"), (512, 256))
    grid.paste(Image.open("7.jpeg"), (0, 512))
    grid.paste(Image.open("8.jpeg"), (256, 512))
    grid.paste(Image.open("9.jpeg"), (512, 512))

    filename = f'{prompt.lower().replace(" ","_")}.{FORMAT}'
    grid.save(filename, FORMAT.upper())
    OPEN = []
    OPEN += VIEWER
    OPEN.append(filename)
    subprocess.Popen(OPEN)

if __name__ == "__main__":
    main()

