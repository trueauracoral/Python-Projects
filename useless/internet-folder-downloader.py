import requests
import re
from urllib.parse import urlparse
import os

url = "https://davidovski.xyz/m/"
folder = urlparse(url).path.replace("/","")
print(folder)
os.mkdir(folder)
html_stuff = requests.get(url).text
links = re.findall('<a href=".+?">', html_stuff)
for link in links:
    link = link.split('"')[1]
    print(link)
    if link.endswith("/"):
        pass
    elif link.startswith(".."):
        pass
    else:
        # I couldn't get os.path.join to work :(
        with open(folder+"/"+link,"wb") as f:
            f.write(requests.get(url+link).content)