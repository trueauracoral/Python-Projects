import requests
import os

url = "https://github.com/terminalforlife"
username = url.split("/")[3]
data = requests.get(f"https://api.github.com/users/{username}/repos").json()
print(username)

os.mkdir(username)
for repo in data:
    print(repo["name"])
    print(repo["description"])
    os.system(f"cd {username} && git clone {repo['html_url']}")