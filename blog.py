# I need to get time instead of asking manuelly for it.
from time import gmtime, strftime
# copy for all platforms
import pyperclip
# Mastodon stuff
from mastodon import Mastodon
# Json for mastodon account
import json

# Inputs
Title = input("Title: ")
Link = input("Link: ")
Date = str(strftime("%a, %d %b %Y %X"))
rssfile = "rss.xml"

# rss file manipulation
with open(rssfile) as r:
  text = r.read().replace("\n</channel>\n</rss>", " ")
with open(rssfile, "w") as w:
  w.write(text)

# Add stuff
with open(rssfile, 'a') as f:
    f.write("\n<item>")
    f.write("\n<title>"+Title+"</title>")
    f.write("\n<link>"+Link+"</link>")
    f.write("\n<guid>"+Link+"</guid>")
    f.write("\n<pubDate>"+Date+"</pubDate>")
    f.write("\n<description>")
    f.write("\n<![CDATA[ <p>Consume this in any software you like!</p> ]]>")
    f.write("\n</description>")
    f.write("\n</item>")
    f.write("\n")
    f.write("\n</channel>")
    f.write("\n</rss>")

# Print file so I can glance and check for errors. Also copy the file to clipboard
f = open('rss.xml', 'r')
content = f.read()
print(content)
pyperclip.copy(content)
f.close()

# Mastodon

# IDK what this does ignore it
Mastodon.create_app(
     'pytooterapp',
     api_base_url = 'https://mastodon.online',
     to_file = 'pytooter_clientcred.secret'
)
mastodon = Mastodon(
    client_id = 'pytooter_clientcred.secret',
    api_base_url = 'https://mastodon.online'
)

# My account password protected by a file that python get's the data from
with open('masto_account.json', 'r') as f:
    data = json.load(f)

mastodon.log_in(
    data['email'],
    data['password'],
    to_file = 'pytooter_usercred.secret'
)
mastodon = Mastodon(
    access_token = 'pytooter_usercred.secret',
    api_base_url = 'https://mastodon.online'
)

# Print the toot so I can see what happened
print(Title+"\n"+Link)
# Send a toot with the Title on the first line and the link at the bottom
mastodon.toot(Title+"\n"+Link)
