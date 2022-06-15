#!/usr/bin/env python
# Going to export org to html

# Neccasary import to convert org to html
from orgpython import to_html

# Inputs
orgfile = input("ORG file: ")

with open(orgfile) as f:
    text = f.read()

# Do stuff
orgfile = orgfile.replace(".org", ".html")

with open(orgfile, 'w') as f:
    f.write(to_html(text, toc=False, offset=0, highlight=True))
 
print(to_html(text, toc=False, offset=0, highlight=True))
