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
