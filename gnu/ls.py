#!/usr/bin/env python
# LS - list files in a directory
import os
import sys

args = sys.argv[1:]
for file in os.listdir():
    if os.path.isdir(file):
        print(file+"/")
    elif file.startswith("."):
        if "-a" in args:
            if os.path.isdir(file):
                print(file+"/")
            else:
                print(file)
        pass
    else:
        print(file)
