# Installed with "pip install pyyaml"
import yaml
import os
browser = "palemoon"

with open('software.yaml') as f:
    data = yaml.load(f, Loader=yaml.FullLoader)
beginning = f"""<!DOCTYPE html>
<head>
<meta http-equiv="Content-Type" content="text/html;charset=utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>{data["title"]}</title>
<link rel="stylesheet" href="{data["css"]}">
</head>

<body>

<h1>{data["title"]}</h1>
"""

items = []
for key, content in data["software"].items():
    item = f"""<h2>{key.replace("_"," ")}</h2>
{content}
"""
    items.append(item)
    final = '\n'.join(items)
    
end = """
<hr>
<footer>
<a rel='license' href='http://creativecommons.org/licenses/by-sa/4.0/'><img alt='Creative Commons License' style='border-width:0' width='88' height='31' src='../images/cc-by-sa.png' /></a><br>
Unless otherwise noted, all content on this website is Copyright Zortazert 2021-2022 and is licensed under <a rel='license' href='http://creativecommons.org/licenses/by-sa/4.0/'>CC BY-SA 4.0</a>.
</footer>
</body>
</html>
"""

filename = data["title"].lower().replace(" ","_")+".html"
with open(filename,"w") as f:
    f.write(beginning+final+end)
os.system(f"{browser} {filename}")
