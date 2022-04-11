import sys
import textwrap
import json
import requests

chadoku = """
                         ___
                     \\__| o \\
                     /   \\  |
                          | |     o
                        __| |__  //
                       |_______|//
                       \\_______//
"""

if len(sys.argv) == 1:
    print("please give an argument to print text")
    quit()
if sys.argv[1] == "fortune":
    text = requests.get("https://helloacm.com/api/fortune/").json().replace("      "," ")
else:
    text = ' '.join(sys.argv[1:])
num = len(text)
dashes = num + 2
if dashes > 19:
    dashes = 42
    print(" " + "-"*dashes)
    text = textwrap.fill(text, dashes-2).split("\n")
    for enter in text:
        stuff = "| " + enter
        length = dashes - len(stuff)
        print(stuff + " "*length+" |")
    print(" " + "-"*dashes)
else:
    print(" " + "-"*dashes)
    print("| " + text + " |")
    print(" " + "-"*dashes)
print(chadoku)
