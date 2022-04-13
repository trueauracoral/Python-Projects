import json
browser = "palemoon"

with open("text.json","r") as f:
    text = json.loads(f.read())

beginning = f"""
<!DOCTYPE html>
<head>
<meta http-equiv="Content-Type" content="text/html;charset=utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>{text["title"]}</title>
<link rel="stylesheet" href="{text["css"]}">
</head>

<body>
"""
print(beginning)
print(text["items"][0]["description"])
for i, item in enumerate(text["items"]):
    print(item)
    print(item[i]["description"])
end = """
<hr>
<footer>
<a rel='license' href='http://creativecommons.org/licenses/by-sa/4.0/'><img alt='Creative Commons License' style='border-width:0' width='88' height='31' src='../images/cc-by-sa.png' /></a><br>
Unless otherwise noted, all content on this website is Copyright Zortazert 2021-2022 and is licensed under <a rel='license' href='http://creativecommons.org/licenses/by-sa/4.0/'>CC BY-SA 4.0</a>.
</footer>
</body>
</html>
"""
