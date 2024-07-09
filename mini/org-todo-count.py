#!/usr/bin/env python
# Simple regex program to parse a org file for all TODO headers and
# print them out nicely. I use it to put into wheelofnames.com
import re # I am not a regex god. yet...
import pyperclip # gigachad

TODO_file = "C:\\SGZ_Pro\\Hobbys\\Writing\\Org\\todo.org"

with open(TODO_file) as f:
    text = f.read()

# Godly regex building the third temple with this one
found = re.findall("\*\* TODO .*",text)

formatted = ""
for i in found:
    formatted += ' '.join(i.split(" ")[2:]) + "\n"

print(formatted)
pyperclip.copy(formatted)

print(f"===LEFT===\nYou have {len(found)} items you need TODO")
