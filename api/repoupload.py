#!/usr/bin/env python
import requests
from requests.auth import HTTPBasicAuth
import os
import argparse

def get_arguments():

    parser = argparse.ArgumentParser(description='repoupload.py upload to an organization repos downloaded')
    parser.add_argument('-u', '--username', type=str, metavar='USER', help='Username for your account on gitea site')
    parser.add_argument('-p', '--password', type=str, metavar='PASSWORD', help='Password for your account on gitea site')
    parser.add_argument('-s', '--site', type=str, metavar='SITE', help='Website where your uploading these repos too a gitea instance.')
    parser.add_argument('-d', '--directory', type=str, metavar='DIRECTORY', help='Directory where your repos are.')
    parser.add_argument('-o', '--organization', type=str, metavar='organization', help='Organization name.')
    args = parser.parse_args()
    return args

def main():

    args = get_arguments()
    for repo in os.listdir(str(args.directory)):
        x = requests.post(f'{args.site}/api/v1/orgs/{args.organization}/repos', json={"name":repo}, auth=HTTPBasicAuth(args.username, args.password))
        print(x.text)
        os.system(f"cd {args.organization} && cd {repo} && git remote set-url origin https://codeberg.org/{args.organization}/{repo}/")
        os.system(f"cd {args.organization} && cd {repo} && git add .")
        os.system(f"cd {args.organization} && cd {repo} && git push --force")
    
if __name__ == '__main__':
    main()
