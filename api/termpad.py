# termpad.py
# This uses the termpad pastebin website to do a variety of things.
#
# Dependencies: curl, xclip (optional).
import os
import subprocess
import argparse
import platform

browser = "palemoon"
parser = argparse.ArgumentParser(description='Termpad curl python script')
parser.add_argument('-g', '--get', type=str, metavar='ID', help='Get a pasted document')
parser.add_argument('-o', '--open', type=str, metavar='ID', help='Open a termpad link in a browser.')
parser.add_argument('-p', '--paste', type=str, metavar='PATH', help='Paste an existing file.')
parser.add_argument('-c', '--copy', action="store_true", default=False, help='Copy the link to the pasted file')
args = parser.parse_args()
if args.get:
    if args.get == "":
        print("Please give a termpad URL/Paste ID")
    elif args.get.startswith("https://termpad.com"):
        if "https://termpad.com/" in args.get:
            paste_id = args.get.split("/")[-1]
        else:
            paste_id = args.get
        text = subprocess.getoutput(f"curl --silent https://termpad.com/raw/{paste_id}")
        print(text)
elif args.paste:
    if os.path.isfile(args.paste):
        paste_url = subprocess.getoutput(f'curl --silent --data-binary @"{args.paste}" termpad.com')
        print(paste_url)
        if args.copy == True:
            if platform.system() == "Windows":
                os.system(f"echo {paste_url} | clip")
            else:
                os.system(f"echo '{paste_url}' | xclip -selection clipboard")
    else:
        print("This is not a file")
elif args.open:
    if args.open.startswith("https://termpad.com"):
        if platform.system() == "Windows":
            os.system(f"start {args.open}")
        else:
            os.system(f"xdg-open {args.open}")
    else:
        print("This is not a termpad URL")
else:
    parser.print_help()
