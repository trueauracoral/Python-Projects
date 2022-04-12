import sys
import textwrap
import random

snake = """
         \\        ___
          \\   \\__| o \\
              /   \\  |
                   | |     o
                 __| |__  //
                |_______|//
                \\_______//
"""
cow = """
        \\   ^__^
         \\  (oo)\\_______
            (__)\\       )\\/\\
                ||----w |
                ||     ||
"""
tux = """
       \\
        \\
            .--.
           |o_o |
           |:_/ |
          //   \\ \\
         (|     | )
        /'\\_   _/`\\
        \\___)=(___/
"""
def error():
    print("ERROR: GIVE ME TEXT!")
    quit()
try:
    sys.argv[1]
except:
    error()
if sys.argv[1] == "fortune":
    import requests
    text = requests.get("https://helloacm.com/api/fortune/").json().replace("      "," ")
    thing = snake
elif sys.argv[1] == "-r" or sys.argv[1] == "-r" and sys.argv[2] == "fortune":
    rand = random.randint(1,3)
    if rand == 1:
        thing = snake
    if rand == 2:
        thing = cow
    if rand == 3:
        thing = tux
    if sys.argv[1] == "-r" and sys.argv[2] == "fortune":
        import requests
        text = requests.get("https://helloacm.com/api/fortune/").json().replace("      "," ")
    else:
        text = ' '.join(sys.argv[2:])
elif sys.argv[1] == "-s":
    thing = snake
    text = ' '.join(sys.argv[2:])
elif sys.argv[1] == "-c":
    thing = cow
    text = ' '.join(sys.argv[2:])
elif sys.argv[1] == "-t":
    thing = tux
    text = ' '.join(sys.argv[2:])
elif sys.argv[1] == "-h" or sys.argv[1] == "--help":
    print("""This is a less feature rewrite of cowsay in python.

python snakesay.py QUERY - make a snake say something

python snakesay.py fortune - make a snake say a random fortune. Requires requests installed.

python snakesay.py -r QUERY - randomly selected a tux, cow or snake will say something
    
python snakesay.py -t QUERY - a tux will say something

python snakesay.py -s QUERY - a snake will say something

python snakesay.py -c QUERY - a cow will say something""")
    quit()
else:
    thing = snake
    text = ' '.join(sys.argv[2:])
    
if text == "":
    error()
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

print(thing)
