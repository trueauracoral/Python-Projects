#!/usr/bin/env python
#
# Requires git and curl
#
# Command stuff:
# curl -X 'POST' -H 'accept: application/json' -H 'Content-Type: application/json' {site}/api/v1/orgs/{orgname}/repos -d '{"name":"{reponame}"}' -u "{username}:{password}"
# cd {dir}
# git remote set-url origin https://codeberg.org/{orgname}/{dir}/
# git add .
# git push
import requests
import os
import argparse
import subprocess
from requests.auth import HTTPBasicAuth

def get_arguments():

    parser = argparse.ArgumentParser(description='repoupload.py upload to an organization repos downloaded')
    parser.add_argument('-u', '--username', type=str, metavar='USER', help='Username for your account on github or gitea site')
    parser.add_argument('-p', '--password', type=str, metavar='PASSWORD', help='Password for your account on github or gitea site')
    parser.add_argument('-s', '--site', type=str, metavar='SITE', help='Website where your uploading these repos too, github or a gitea instance.')
    parser.add_argument('-d', '--directory', type=str, metavar='DIRECTORY', help='Directory where your repos are.')
    parser.add_argument('-o', '--organization', type=str, metavar='organization', help='Organization name.')
    #parser.add_argument('-r', '--releases', action="store_true", default=False, help='Fetch the newest release from github/gitea repo')
    args = parser.parse_args()
    return args

def main():

    args = get_arguments()
    for repo in os.listdir(str(args.directory)):
        x = requests.post(f'{args.site}/api/v1/orgs/{args.organization}/repos', json={"name":repo}, auth=HTTPBasicAuth(args.username, args.password))
        print(x.text)
        #curl_command = f"curl -X 'POST' -H 'accept:application/json' -H 'Content-Type:application/json' {args.site}/api/v1/orgs/{args.organization}/repos -d '{{\"name\":\"{repo}\"}}' -u '{args.username}:{args.password}'"
        #print(curl_command)
        #os.system(str(curl_command))
        os.system(f"cd {args.organization} && cd {repo} && git remote set-url origin https://codeberg.org/{args.organization}/{repo}/")
        os.system(f"cd {args.organization} && cd {repo} && git add .")
        os.system(f"cd {args.organization} && cd {repo} && git push --force")
    
if __name__ == '__main__':
    main()
