#!/usr/bin/env python
import requests

# Try and get 1920x1080. Set this to True if you want that. You will
# get images by having this turned on.
high=False

search = input("Wallhaven search: ")
data = requests.get(f"https://wallhaven.cc/api/v1/search?q={search}").json()

num = 0
for i, wallpaper in enumerate(data["data"]):
    url = wallpaper["path"]
    if wallpaper["resolution"] == "1920x1080" and high == True:
        num = num+1
        file = f"{num}.{url.split('.')[3]}"
        print(url)
        print(file)
    else:
        file = f"{i}.{url.split('.')[3]}"
        print(url)
        print(file)
    with open(file,"wb") as f:
        f.write(requests.get(url).content)
