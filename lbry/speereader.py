"""
How to run this script.
1. Install with pip the requests and markdown module
2. In the browser variable specify your browser to something that can be ran in your shell
3. In the file variable specify where you want the html file to go.
4. Put a styles.css file in this directory.
5. Finally run this script with python.
"""

# Make sure you pip install this
import requests
import markdown
import subprocess

browser = 'c:\\users\\stanl\\appData\\local\\bravesoftware\\brave-browser\\application\\brave.exe'
link = input("Link: ")
md = str(requests.get(link).text.rstrip())
html = markdown.markdown(md)
file = "C:\\SGZ_Pro\\Hobbys\\coding-projects\\Python\\lbry\\markdown.html"

with open ('markdown.html', 'w') as f:
    f.write(html)

with open(file,'r') as contents:
      save = contents.read()
with open(file,'w') as contents:
      contents.write("<!DOCTYPE html>\n<head>\n<meta http-equiv='Content-Type' content='text/html;charset=utf-8' />\n<meta name='viewport' content='width=device-width, initial-scale=1' />\n<link rel='stylesheet' href='./styles.css'>")
with open(file,'a') as contents:
      contents.write(save)

subprocess.Popen([browser, file])
