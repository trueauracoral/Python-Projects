import requests
import re
import os

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:17.0) Gecko/20121201 icecat/17.0.1'}

link = "https://www.4shared.com/folder/-F9L_kva/004/Sub.html?detailView=false&sortAsc=true&sortsMode=NAME"

data = str(requests.get(link).content)

subdirs = re.findall('<a href=".+?" class="jsFolderLink gaClick"',data)
print(subdirs)
name = 0
for i, subdir in enumerate(subdirs):
    if not subdir.startswith("<a href="):
        pass
    elif "javascript" in subdir.split('"')[1]:
        pass
    elif i == 1:
        break
    else:
        name = name+1
        print(subdir.split('"')[1])
        data2 = str(requests.get(subdir.split('"')[1],headers=headers).content)
        video = re.findall('href="https://www.4shared.com/video/.+?"',data2)
        print(video)
        video = video[0].split('"')[1]
        os.system(f"yt-dlp {video}")