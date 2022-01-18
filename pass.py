"""
This is a script for me to generate passwords. I advise you to maybe make your own script for generating passwords for max security.
"""
import random
# Does not come with python. Go to install this.
import pyperclip

# Gives me a password.
keys = ("abcdefghijklmnopqrxtuvwsyz" + "ABCDEFGHIJKLMNOPQRXTUV" + "1234567890" + "~!@#$%^&*[]{}()")
phrase = ("".join(random.sample(keys,16)))

# Get some data about what is this account
account = input("Account: ")
username = input("Username: ")

# Open org file and start adding things
with open("pasec.org", 'a') as f:
    f.write("\n* " + account)
    f.write("\n- Username: " + username)
    f.write("\n- Pass: " + phrase)

print(phrase + "\nDelete this now somehow")
pyperclip.copy(phrase)
