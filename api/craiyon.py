#!/usr/bin/env python
import requests
import base64
import sys

headers = {
    "authority": "backend.craiyon.com",
    "accept": "application/json",
    "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
    "content-type": "application/json",
    "origin": "https://www.craiyon.com",
    "referer": "https://www.craiyon.com/",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15",
}

data = requests.post("https://backend.craiyon.com/generate", headers=headers, json={"prompt": ' '.join(sys.argv[1:])}).json()

for i, image in enumerate(data["images"]):
    image = image.replace('"','').replace("\\n","\n")
    with open(f"{i}.txt","w") as f:
        f.write(image)
    decodedata = base64.b64decode(image)
    with open(f"{i}.jpeg","wb") as f:
        f.write(decodedata)
