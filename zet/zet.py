#!/usr/bin/env python
# zet.py
# This script will help me manage a zettelkasten.
#
# Missing:
# -d, --delete  delete a note
# -o, --open    open a note
# -n, --new     new note
# -e, --edit    edit a note
# -l, --last    Show last note
# -E, --export  export your notes
import os
import subprocess
from datetime import datetime
import argparse
import sys

editor = "emacs"
extension = "org"
document_start = """#+TITLE: %TITLE%
#+OPTIONS: toc:nil num:nil 

"""

#parser.add_argument('-l', '--list', type=str, metavar='ID', help='Open a termpad link in a browser.')
parser = argparse.ArgumentParser(description='zet.py Zettelkalsten Generator.')
parser.add_argument('-t', '--titles', action="store_true", default=False, help='list all titles of your ntoes in the zettelkasten')
parser.add_argument('-n', '--new', action="store_true", default=False, help='create a new note in your zettelkasten')
args = parser.parse_args()

if args.new:
    date = datetime.now().strftime("%Y%m%d%H%M%S")    
    os.mkdir(date)
    title = input("Temporary title for the new zet: ")
    file_location = os.path.join(os.getcwd(),date,f"README.{extension}")
    with open(file_location,"w") as f:
        f.write(document_start.replace("%TITLE%",title))
    
    os.popen(f'{editor} {file_location}')
elif args.titles:
    for path, subdirs, files in os.walk(str(os.getcwd())):
        for name in files:
            if name == sys.argv[0]:
                pass
            else:
                with open(os.path.join(path,name)) as f:
                    title = ' '.join(f.read().splitlines()[0].split(" ")[1:])
                print(f"[{os.path.basename(path)}] {title}")