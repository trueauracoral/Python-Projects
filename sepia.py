# Imports
import requests
import json
import os

# Coloring
bold="\033[01m"
norm="\033[00m"
bright_cyan="\033[46m"
colora="\033[45m"
colorb="\033[44m"

# Variables
query = input("Searching for: ")
query = str(query)
size = str(19)
search = "https://sepiasearch.org/api/v1/search/videos?search=" + query
command = "mpv "

data = requests.get(search)
json_stuff = json.loads(data.text)
for i, vid in enumerate(json_stuff["data"]):
    print(i, colora+vid["name"]+norm+"\n"+colorb+vid["channel"]["displayName"]+norm+"\n"+bright_cyan+vid["url"]+norm)

# Choose a result
c = 100000
while not c >= 0 or not c <= 19:
    c = input('Number from 1-' + size + " of the URL you want to open: ")
    try:
            c = int(c)
    except:
            c = 100000

selected_url = json_stuff["data"][c]["url"]
comments = "https://" + json_stuff["data"][c]["account"]["host"] + "/api/v1/videos/" + json_stuff["data"][c]["uuid"] + "/comment-threads/"
data_comment = requests.get(comments)
json_comment = json.loads(data_comment.text)
# PRINT COMMENTS!
for i, comment in enumerate(json_comment["data"]):
    # Sometimes peertube likes to give nonsese json that I don't
    # understand even why it's there so this detects that it prints no
    # account data.
    if comment["account"] == None:
        print(i, "No Account Data")

    # This detects if a comment has replies. If the totalReplies value
    # is greater than 0 it will get the id and add it to the link to
    # see the whole thread aka replies
    elif comment["totalReplies"] > 0:
        # Fetching replies
        replies = comments + str(comment["id"])
        data_replies = requests.get(replies)
        json_replies = json.loads(data_replies.text)
        total_replies = str(json_replies["comment"]["totalReplies"])
        # Print out that this comment has replies and also say how many
        print(i, colora+comment["account"]["displayName"]+norm+"\n"+colorb+comment["text"]+norm+bright_cyan+"\nREPLIES: "+total_replies+norm)
        # Here in this for loop inside of a for loop we start to print
        # out the replies.
        for i, reply in enumerate(json_replies["children"]):
            # Same thing can happen where it gives nonsense json.
            if reply["comment"]["account"] == None:
                print(i, "No Account Data")
            # This prints out the first reply.
            else:
                print(" " + str(i) + " " + colora+reply["comment"]["account"]["displayName"]+norm+"\n "+colorb+reply["comment"]["text"]+norm)

    # This is the final thing, the comment has no replys so it just
    # prints it as a comment.
    else:
        print(i, colora+comment["account"]["displayName"]+norm+"\n"+colorb+comment["text"]+norm)

os.system(command + selected_url)
