import requests
import json
api = "https://api.urbandictionary.com/v0/define?term=ratio%27d"
data = requests.get(api)
json_stuff = json.loads(data.text)
for result in json_stuff["list"]:
    print(result["word"]+"\n"+result["definition"]+"\n"+result["example"])
