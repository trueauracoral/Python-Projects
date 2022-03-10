import requests
import json
query = input("Word: ")
api = f"https://api.urbandictionary.com/v0/define?term={query}"
data = requests.get(api)
json_stuff = json.loads(data.text)
for i, result in enumerate(json_stuff["list"]):
    print(result["word"]+"\n"+result["definition"]+"\n"+result["example"])
    if i == 1:
        break
