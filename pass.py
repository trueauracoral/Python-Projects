import random
import string

keys = (string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation)

print("".join(random.sample(keys,16)))
