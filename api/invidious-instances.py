# Using the invidious instance API it prints out most likely working 
# and healthy invidious instances.
import requests

url = "https://api.invidious.io/instances.json"
data = requests.get(url).json()

for i, instance in enumerate(data):
    if instance[1]["type"] == "onion":
        pass
    elif float(instance[1]["monitor"]["30dRatio"]["ratio"]) > float(90):
        print(instance[1]["uri"])