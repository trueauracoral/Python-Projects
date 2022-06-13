import os
import subprocess
from datetime import datetime
import argparse

editor = "emacs"
extension = "org"
document_start = """#+TITLE: %TITLE%
#+OPTIONS: toc:nil num:nil 

"""

#parser.add_argument('-l', '--list', type=str, metavar='ID', help='Open a termpad link in a browser.')
parser = argparse.ArgumentParser(description='zet.py Zettelkalsten Generator.')
parser.add_argument('-l', '--list', action="store_true", default=False, help='List your notes in the zettelkasten')
parser.add_argument('-n', '--new', action="store_true", default=False, help='Create a new note in your zettelkasten')
args = parser.parse_args()

def create():
    date = datetime.now().strftime("%Y%m%d%H%M%S")    
    os.mkdir(date)
    title = input("Temporary title for the new zet: ")
    file_location = os.path.join(os.getcwd(),date,f"README.{extension}")
    print(file_location)
    with open(file_location,"w") as f:
        f.write(document_start.replace("%TITLE%",title))
    
    subprocess.Popen(f'{editor} {file_location}')

if args.new:
    create()
#elif args.list:
#    list()