#!/usr/bin/env python
import random
import pyperclip
import re
import sys
import argparse

password_file = "drowsapp.org"

def parse_arguments():
    parser = argparse.ArgumentParser(description='pass.py')
    parser.add_argument('-f', '--find', type=str, metavar='NAME', help='Find password credentials')
    parser.add_argument('-n', '--new', action="store_true", default=False, help='Create a new account credentials')
    args = parser.parse_args()

    return args

def main():
    args = parse_arguments()
    if args.new:
        keys = ("abcdefghijklmnopqrxtuvwsyz" + "ABCDEFGHIJKLMNOPQRXTUV" + "1234567890" + "~!@#$%^&*[]{}()")
        phrase = ("".join(random.sample(keys,16)))

        account = input("Account: ")
        username = input("Username: ")

        with open(password_file, 'a') as f:
            f.write("\n* " + account)
            f.write("\n- Username: " + username)
            f.write("\n- Pass: " + phrase)

        print(phrase + "\nDelete this now somehow")
        pyperclip.copy(phrase)

    if args.find:
        with open(password_file) as f:
            passwords = f.read()
        headers = passwords.split("* ")
        for line in headers:
            if args.find in line.split(" ")[0].split("\n-")[0].lower():
                print('\n'.join(line.replace("- ","").splitlines()))

if __name__ == "__main__":
    main()
