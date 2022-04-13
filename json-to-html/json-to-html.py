import os
import json

browser = "palemoon"

with open("settings.json","r") as f:
    settings = json.loads(f.read())
beginning = f"""<!DOCTYPE html>
<head>
<meta http-equiv="Content-Type" content="text/html;charset=utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>{settings["title"]}</title>
<link rel="stylesheet" href="{settings["css"]}">
</head>

<body>

<h1>{settings["title"]}</h1>
"""
files = os.listdir()
definitions = []
for i, file in enumerate(files):
    if file == "settings.json":
        pass
    elif file.endswith(".json") == True:
        print(file)
        with open(file,"r") as f:
            item = json.loads(f.read())
        definition = f"""<h2>{item["name"]}</h2>
<ul>
<li><b>Definition</b>: {item["description"]}</li>
<li><b>Quote</b>: "{item["quote"]}"</li>
</ul>
"""
        definitions.append(definition)
        definition = '\n'.join(definitions)
    
end = """
<hr>
<footer>
<a rel='license' href='http://creativecommons.org/licenses/by-sa/4.0/'><img alt='Creative Commons License' style='border-width:0' width='88' height='31' src='../images/cc-by-sa.png' /></a><br>
Unless otherwise noted, all content on this website is Copyright Zortazert 2021-2022 and is licensed under <a rel='license' href='http://creativecommons.org/licenses/by-sa/4.0/'>CC BY-SA 4.0</a>.
</footer>
</body>
</html>
"""

with open("index.html","w") as f:
    f.write(beginning+definition+end)
os.system(browser + " index.html")
