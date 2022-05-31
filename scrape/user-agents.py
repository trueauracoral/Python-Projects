import requests
import re

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:17.0) Gecko/20121201 icecat/17.0.1'}

data = str(requests.get("https://user-agents.net/random",headers=headers).content)

#user_agents = re.findall('<a href="/string/.+?">.+?</a>',data)
link = re.findall('<a href="/string/.+?</a>(.+?)</a>',data)
cleaner = re.compile('<.*?>')
final = re.sub(cleaner, '', link[0])
print(final.replace("\\n","").replace("\\t",""))