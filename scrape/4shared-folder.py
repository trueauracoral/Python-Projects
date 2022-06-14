import requests
import re
import os

link = "https://www.4shared.com/folder/-F9L_kva/004/Sub.html?detailView=false&sortAsc=true&sortsMode=NAME"
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:17.0) Gecko/20121201 icecat/17.0.1'}
data = str(requests.get(link).content)
subdirs = re.findall('<a href=".+?" class="jsFolderLink gaClick"',data)
name = 0
for i, subdir in enumerate(subdirs):
    if not subdir.startswith("<a href="):
        pass
    elif "javascript" in subdir.split('"')[1]:
        pass
    else:
        data2 = str(requests.get(subdir.split('"')[1],headers=headers).content)
        video = re.findall('href="https://www.4shared.com/video/.+?"',data2)
        video = video[0].split('"')[1]
        os.system(f"yt-dlp {video}")