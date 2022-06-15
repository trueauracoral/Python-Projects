#!/usr/bin/env python
import requests
import json

fetch = {
  "jsonrpc": "2.0",
  "id": 1,
  "method": "comment.List",
  "params": {
      "page":1,
      "top_level": False, # For comment replies
      "parent_id": "parent comment ID", # For comment replies
      "claim_id":"463e63afb35a319f260b36ef8d5c3dc41a98ce28",
      "page_size":99999,
      "channel_id":"ecf0a6be99030d0ad4e10aec11d2c0bab94246ae",
      "channel_name":"@MusicARetro"
  }
}

data = requests.post("https://comments.odysee.com/api/v2?m=comment.List", data = fetch)
print(data.text)
json_stuff = json.loads(data.text)
print(json_stuff)
