import random
import string

# Gives me a password.
keys = (string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation)
phrase = ("".join(random.sample(keys,16)))

# Get some data about what is this account
account = input("Account: ")
username = input("Username: ")

# Open org file and start adding things
with open("pasec.org", 'a') as f:
    f.write("\n* " + account)
    f.write("\n- Username: " + username)
    f.write("\n- Pass: " + phrase)
