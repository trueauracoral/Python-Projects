#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import platform

file = input("File: ")
if platform.system() == "Windows":
    git_bash_shell = "%LocalAppData%\\Programs\\Git\\bin\\sh.exe"
    os.system(f'{git_bash_shell} -c "iconv -f utf-8 -t utf-8 -c "{file}" > "{file}.new" && mv -f "{file}.new" "{file}""')
    os.system(f'{git_bash_shell} -c "rm -rf "{file}.new""')
else:
    os.system(f'iconv -f utf-8 -t utf-8 -c "{file}" > "{file}.new" && mv -f "{file}.new" "{file}""')
    os.system(f'rm -rf "{file}.new"')

with open(file) as f:
    data = f.read()

if "é" in data:
    # More characters like this in the future. For now this is kind of
    # stupid.
    data = data.replace("é","e")

with open(file, "w") as f:
    f.write(data)
