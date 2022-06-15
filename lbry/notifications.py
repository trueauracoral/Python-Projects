#!/usr/bin/env python
import json
import requests

with open('auth_token.json', 'r') as f:
    json_stuff = json.load(f)

auth_token = json_stuff["auth_token"]

notifications = requests.post("https://api.odysee.com/notification/list", data={"auth_token":auth_token}).json()

#print(json.dumps(notifications, indent=4))

for i in notifications["data"]:
    if i["is_read"] == "true":
        print("--")
        print(i["notification_parameters"]["device"]["title"])
        print(i["notification_parameters"]["device"]["target"])
        print(i["notification_parameters"]["device"]["text"])
    else:
        print("No new notifications!")
        break
