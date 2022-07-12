#!/usr/bin/env python
# I got the json file by clicking backup bookmarks in palemoon. Maybe
# this can work generally in firefox browsers idk.

import json
backup = "c:\\sgz_Pro\\Hobbys\\Writing\\Org\\bookmarks-2022-07-12.json"

with open(backup, encoding="utf-8") as f:
    text = f.read()
json_stuff = json.loads(text)

with open("index.html","w") as f:
    f.write("<h1>Bookmarks Toolbar</h1>")

for i, bookmark in enumerate(json_stuff["children"][1]["children"]):
    print(i)
    if bookmark["type"] == "text/x-moz-place":
        with open("index.html","a") as f:
            if bookmark["title"] != "":
                f.write(f"\n<p><a href='{bookmark['uri']}'>{bookmark['title']}</a></p>")
            else:
                f.write(f"\n<p><a href='{bookmark['uri']}'>{bookmark['uri']}</a></p>")
    elif bookmark["type"] == "text/x-moz-place-separator":
        with open("index.html","a") as f:
            f.write("\n<hr>")
    elif bookmark["type"] == "text/x-moz-place-container":
        with open("index.html","a") as f:
            f.write(f"\n<h2>{bookmark['title']}</h2>\n<ul>")
            for item in bookmark["children"]:
                f.write(f"<li><a href='{item['uri']}'>{item['title'].encode('utf-8').decode('ascii','ignore')}</a></li>")
            f.write("\n</ul>")    
