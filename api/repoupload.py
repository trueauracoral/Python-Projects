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
    for i, repo in enumerate(os.listdir(str(args.directory))):
        os.system(f"curl -X 'POST' -H 'accept:application/json' -H 'Content-Type:application/json' {args.site}/api/v1/orgs/{args.organization}/repos -d '{{\"name\":\"{repo}\"}}' -u '{args.username}:{args.password}'")
        os.system(f"cd {repo} && git remote set-url origin https://codeberg.org/{args.organization}/{repo}/")
        os.system(f"cd {repo} && git add .")
        os.system(f"cd {repo} && git push")
    
if __name__ == '__main__':
    main()
