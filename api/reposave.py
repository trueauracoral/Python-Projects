# What do you need to run this script:
# - python
# - python requests
# - a valid GitHub URL e.g. "https://github.com/<USER>"
# - git
# More information:
# This script was created after TerminalForLife deleted his YouTube
# channel all of it everything very sad. So while his github is still
# working why not back it up. This includes forked repos and Public
# Archives. Just everything. I might make a Codeberg account or
# something like that to put all of his repos it will just be time
# consuming at less there is some git command to create a repo.
import requests
import os

url = "https://github.com/lukesmithxyz"
username = url.split("/")[3]
data = requests.get(f"https://api.github.com/users/{username}/repos").json()
print(username)

os.mkdir(username)
for repo in data:
    print(repo["name"])
    print(repo["description"])
    os.system(f"cd {username} && git clone {repo['clone_url']}")
