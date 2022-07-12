# HOW TO USE THIS SCRIPT
#
# You can't export your skype messages DIRECTLY inside skype for some
# reason. So I searched on the internet how to export messages from
# skype and found this page from microsoft's support website
# https://support.skype.com/en/faq/FA34894/how-do-i-export-or-delete-my-skype-data. It's
# a lot of extra steps it lists to use their weird JS tool to view the
# content. You can't even download it after except by doing Control +
# P a lot on all your things. Which won't even do you well because
# it's not going to show you the whole list of messages. So I present
# to you my script.

# 1. Go to the export page and sign into your microsoft account.
# https://go.skype.com/export

# 2. Select download your Conversations. Wait a bit and it will give
# you a tar link to download.

# 3. Extract the tar using your method of tar extraction. They list to
# use some command line option. If it failes on one file look for some
# option to keep the files. It should give you a new file called
# "messages.json"

# 4. Install python and run this script. python FILEOFTHISSCRIPT

# 5. Now then there will be a index.html file generated and click on
# the links for all your messages. You should also see a bunch of
# other html files were downloaded. You could in your browser export
# them as PDF or do whatever you want. It has who it was from, date
# and content in plaintext.
import json
import urllib.parse
import os.path

file = "C:/SGZ_Pro/Skype chats/messages.json"
with open(file,encoding="utf8") as f:
    data = json.loads(f.read())

with open("index.html","w") as f:
    f.write("<h1>Skype Chats</h1>\n")

for conversation in data["conversations"]:
    print(conversation["displayName"])
    file_name = str(conversation["displayName"]).replace(":","").replace(",","")+".html"
    with open(file_name,"w") as f:
        f.write(f"<h1>{conversation['displayName']}</h1>\n")
    files = os.listdir("media")
    for message in conversation["MessageList"]:
        with open(file_name,"a") as f:
            if message['messagetype'] == "RichText/UriObject":
                try:
                    image = message["content"].split('doc_id="')[1].split('"')[0]
                    for file in files:
                        if file.endswith(".json"):
                            pass
                        else:
                            if image in file:
                                f.write(f'<img src="./media/{file}" width=50% height=auto>')
                except:
                    print("ERROR")
            else:
                f.write(f"<h2>{message['from']} on {message['originalarrivaltime']}</h2>\n<p>{message['content'].encode('utf-8').decode('ascii','ignore')}</p>")
    with open("index.html","a") as f:
        f.write(f"<li><a href='./{urllib.parse.quote(file_name)}'>{conversation['displayName']}</a></li>")
