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
    username = urlparse(args.github).path.replace("/","",1)
    api_url = "https://api.github.com"
    if args.releases:
        get_releases = True
        get_repos = False
    else:
        get_repos = True
        get_releases = False
elif args.gitea and "/" in args.gitea:
    username = urlparse(args.gitea).path.replace("/","",1)
    api_url = f"{urlparse(args.gitea).scheme}://{urlparse(args.gitea).netloc}/api/v1"
    if args.releases:
        get_releases = True
        get_repos = False
    else:
        get_repos = True
        get_releases = True
else:
    print("Please tell what gitea server is this from e.g. https://domain.name/USER")
    quit()
if get_repos == True:
    data = requests.get(f"{api_url}/users/{username}/repos").json()
    print(username)
    
    os.mkdir(username)
    for repo in data:
        print(repo["name"])
        print(repo["description"])
        os.system(f"cd {username} && git clone {repo['clone_url']}")
if args.releases:
    print(f"{api_url}/repos/{username}/releases")
    data = requests.get(f"{api_url}/repos/{username}/releases").json()
    assets=[]
    for asset in data[0]['assets']:
        assets.append(f"{asset['name']} - {asset['browser_download_url']}")
    assets = '\n'.join(assets)
    print(f"""Release Number: {data[0]['tag_name']}
Release Name: {data[0]['name']}
---
[0] Tarball: {data[0]['tarball_url']}
[1] Zipball: {data[0]['zipball_url']}
Assets:
[2] {assets}""")
    try:
        choice = int(input("Download: "))
    except:
        print("Has to be an integer")
    if choice == 1:
        