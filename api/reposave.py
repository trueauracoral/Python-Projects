#!/usr/bin/env python
#
# Requires git
import requests
import os
import argparse
from urllib.parse import urlparse

parser = argparse.ArgumentParser(description='reposave.py Download stuff from git repos')
parser.add_argument('-gh', '--github', type=str, metavar='USER', help='Download all of a user\'s repos from github')
parser.add_argument('-gt', '--gitea', type=str, metavar='SERVER/USER', help='Download all of a user\'s repos from gitea')
parser.add_argument('-r', '--releases', action="store_true", default=False, help='Copy the link to the pasted file')
args = parser.parse_args()

if args.github:
    username = args.github
    api_url = "https://api.github.com"
elif args.gitea:
    if "/" in args.gitea:
        username = urlparse(args.gitea).path.split("/")[1]
        api_url = f"{urlparse(args.gitea).scheme}://{urlparse(args.gitea).netloc}/api/v1"
    else:
        print("Please tell what gitea server is this from e.g. https://domain.name/USER")
        quit()
data = requests.get(f"{api_url}/users/{username}/repos").json()
print(username)

os.mkdir(username)
for repo in data:
    print(repo["name"])
    print(repo["description"])
    os.system(f"cd {username} && git clone {repo['clone_url']}")
