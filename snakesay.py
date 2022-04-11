import sys
import textwrap

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
else:
    text = ' '.join(sys.argv[1:])
    num = len(text)
    dashes = num + 2
    if dashes > 19:
        dashes = 21
        print(" " + "-"*dashes)
        text = textwrap.fill(text, 19).split("\n")
        for enter in text:
            stuff = "| " + enter
            length = 21 - len(stuff)
            print(stuff + " "*length+" |")
        print(" " + "-"*dashes)
    else:
        print(" " + "-"*dashes)
        print("| " + text + " |")
        print(" " + "-"*dashes)
    print(chadoku)
