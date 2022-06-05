# termpad.py
# This uses the termpad pastebin website to do a variety of things.
#
# Dependencies: curl
import os
import subprocess
import argparse

browser = "palemoon"
parser = argparse.ArgumentParser(description='Termpad curl python script')
parser.add_argument('-g', '--get', type=str, metavar='ID', help='Get a pasted document')
parser.add_argument('-o', '--open', type=str, metavar='ID', help='Open a pasted document in a browser.')
parser.add_argument('-p', '--paste', type=str, metavar='PATH', help='Paste an existing file.')
args = parser.parse_args()
 
if args.get:
    if args.get == "":
        print("Please give a termpad URL/Paste ID")
    elif args.get.startswith("https://termpad.com"):
        paste_id = args.get.split("/")[-1]
        text = subprocess.getoutput(f"curl --silent https://termpad.com/raw/{paste_id}")
        print(text)
elif args.paste:
    if args.paste == "":
        print("Please give a file")
    else:
        if os.path.isfile(args.paste):
            paste_url = subprocess.getoutput(f'curl --silent --data-binary @"{args.paste}" termpad.com')
            print(paste_url)
        else:
            print("This is not a file")
elif args.open:
    if args.open.startswith("https://termpad.com"):
        os.system(f"{browser} {args.open}")
    else:
        print("This is not a termpad URL")
else:
    parser.print_help()