#!/usr/bin/env python
"""
This is a script for me to generate passwords. I advise you to maybe make your own script for generating passwords for max security.
"""
import random
import pyperclip
import re
import sys

if len(sys.argv) == 1:
    keys = ("abcdefghijklmnopqrxtuvwsyz" + "ABCDEFGHIJKLMNOPQRXTUV" + "1234567890" + "~!@#$%^&*[]{}()")
    phrase = ("".join(random.sample(keys,16)))

    account = input("Account: ")
    username = input("Username: ")

    with open("drowsapp.org", 'a') as f:
        f.write("\n* " + account)
        f.write("\n- Username: " + username)
        f.write("\n- Pass: " + phrase)

    print(phrase + "\nDelete this now somehow")
    pyperclip.copy(phrase)

elif sys.argv[1] == "-f":
    with open("drowsapp.org") as f:
        passwords = f.read()
    passwords = passwords.splitlines()
    find = input("Which password do you need? ")
    for line in passwords:
        if find in line:
            print("FOUND: "+line.replace("* ",""))
            print(passwords[passwords.index(line)+1].replace("- ",""))
            print(passwords[passwords.index(line)+2].replace("- ",""))

    if find not in passwords:
        print("ERROR: Could not find password you wanted.")
else:
    print("ERROR")
