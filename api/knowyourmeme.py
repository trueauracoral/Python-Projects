import requests
import re

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
query = "linux"
search = f"https://knowyourmeme.com/search?q={query}"
search_result = requests.get(search, headers=headers)
search_data = str(search_result.content)
if "No results" in search_data:
    print("Nothing found :(")
    quit()
links = re.findall('<a href="/memes/.+?">',search_data)
for i, link in enumerate(links[15:]):
    url = "https://knowyourmeme.com"+link.replace("<a href=\"", "").replace("\">", "")
    print(i, url)
    if i == 15:
        break

c = int(input(f"Which meme from 0-{i}: "))
selected = "https://knowyourmeme.com"+links[c+15].replace("<a href=\"", "").replace("\">", "")
print(selected)
#url = 'https://knowyourmeme.com/memes/linus-selfie'
#result = requests.get(url, headers=headers)
#data = str(result.content)
#
#paragraph = re.findall('<p>(.+?)</p>',data)
#cleaner = re.compile('<.*?>')
#about = re.sub(cleaner, '', paragraph[2])
#print("About: " + about)
#origin = re.sub(cleaner, '', paragraph[3])
#print("\nOrigin: " + origin)
#spread = re.sub(cleaner, '', paragraph[4])
