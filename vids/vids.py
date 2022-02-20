# Script for searching YouTube through the invidious and piped API,
# LBRY through lighthouse and librarianAPI and peertube through the
# SepiaSearch API. Played with mpv or whatever program on the computer
# you want.
import requests
import json
import os
import sys

# Use some program. (I recomend mpv for videos)
command = "mpv "
# Your prefered librarian instance
librarian_instance = "https://lbry.mutahar.rocks/"
# Your prefered invidious instance.
invidious_instance = "https://invidio.xamh.de/"
# You need two urls from your piped instance provider: pipedapi url
# and piped instance url.
pipedapi_instance = "https://pipedapi.kavin.rocks/"
piped_instance = "https://piped.kavin.rocks/"
# If you want to see thumbnails (peertube for now). To see thumbnails
# of peertube videos turn this to True
open_thumbs = False
# Your Image viewer. Make sure it can handle file names with no file
# extensions.
image_viewer = "mspaint "
# Temporary Directory File. Full file name of where you want the
# thumbnail to be constantly overwritten to. On GNU/Linux I think it's
# located in the root directory as /tmp/
temp_dir = "C:\\Users\\Stanl\\AppData\\Local\\Temp\\thumbnail"

# C O L E R S
bold = "\033[01m"
norm = "\033[00m"
bright_cyan = "\033[46m"
colora = "\033[45m"
colorb = "\033[44m"

try:
    if sys.argv[1] == "-i":
        try:
            query = sys.argv[2]
        except:
            query = input("Searching for: ")
            query = str(query)
        size = str(19)
        invidious_search = invidious_instance + "api/v1/search?q=" + query

        data = requests.get(invidious_search)
        json_stuff = json.loads(data.text)
        for i, vid in enumerate(json_stuff):
            print(i, colora+vid["title"]+norm+"\n"+colorb+vid["author"]+norm+"\n"+bright_cyan+invidious_instance[:-1]+"/watch?v="+vid["videoId"]+norm)

        c = 100000
        while not c >= 0 or not c <= 19:
            c = input('Number from 1-' + size + " of the URL you want to open: ")
            try:
                    c = int(c)
            except:
                    c = 100000

        comments = invidious_instance + "api/v1/comments/" + json_stuff[c]["videoId"]
        data_comment = requests.get(comments)
        json_comment = json.loads(data_comment.text)
        if "error" in json_comment:
            print("could not fetch comments")
        else:
            for i, comment in enumerate(json_comment["comments"]):
                print(i, colora+comment["author"]+norm+"\n"+colorb+comment["content"]+norm)

        selected_url = invidious_instance + json_stuff[c]["videoId"]
        print(selected_url)
        print("\n"+colora+"DESCRIPTION:\n"+norm+json_stuff[c]["description"])
        os.system(command + selected_url)
        quit()

    elif sys.argv[1] == "-pt":
        try:
            query = sys.argv[2]
        except:
            query = input("Searching for: ")
            query = str(query)
        size = str(19)
        search = "https://sepiasearch.org/api/v1/search/videos?search=" + query
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

        comments = "https://" + json_stuff["data"][c]["account"]["host"] + "/api/v1/videos/" + json_stuff["data"][c]["uuid"] + "/comment-threads/"
        data_comment = requests.get(comments)
        json_comment = json.loads(data_comment.text)
        # PRINT COMMENTS!
        for i, comment in enumerate(json_comment["data"]):
            # Sometimes peertube likes to give nonsese json
            if comment["account"] == None:
                pass

            # This detects if a comment has replies.
            elif comment["totalReplies"] > 0:
                replies = comments + str(comment["id"])
                data_replies = requests.get(replies)
                json_replies = json.loads(data_replies.text)
                total_replies = str(json_replies["comment"]["totalReplies"])
                # Print out that this comment has replies and also say how many
                print(i, colora+comment["account"]["displayName"]+norm+"\n"+colorb+comment["text"]+norm+bright_cyan+"\nREPLIES: "+total_replies+norm)
                # Here in this for loop inside of a for loop for replys
                for i, reply in enumerate(json_replies["children"]):
                    # Same thing can happen where it gives nonsense json.
                    if reply["comment"]["account"] == None:
                        pass
                    # This prints out the first reply.
                    else:
                        print(" " + str(i) + " " + colora+reply["comment"]["account"]["displayName"]+norm+"\n "+colorb+reply["comment"]["text"]+norm)

            # This is the final thing, the comment has no replys so it just
            # prints it as a comment.
            else:
                print(i, colora+comment["account"]["displayName"]+norm+"\n"+colorb+comment["text"]+norm)

        if open_thumbs == True:
            thumbnail_data = requests.get(json_stuff["data"][c]["previewUrl"])
            with open(temp_dir, 'wb') as f:
                f.write(thumbnail_data.content)
            os.system(image_viewer + temp_dir)

        selected_url = json_stuff["data"][c]["url"]
        print("\n"+selected_url)
        print("\n"+colora+"DESCRIPTION:\n"+norm+json_stuff["data"][c]["description"])
        os.system(command + selected_url)

    elif sys.argv[1] == "-l":
        try:
            query = sys.argv[2]
        except:
            query = input("Searching for: ")
            query = str(query)
        size = str(30)
        search = 'https://lighthouse.lbry.com/search?s=' + query + '&include=channel,channel_claim_id,title,description&size=' + size

        data = requests.get(search)
        json_stuff = json.loads(data.text)

        # Results
        for i, x in enumerate(json_stuff):
            pre = "lbry://"
            if x["channel"]:
                pre += x["channel"] + "/"
            url = pre + x["name"]
            print(i, bright_cyan+x["title"]+norm+"\n"+url)

        # Choose a result
        c = 100000
        while not c >= 0 or not c <= 29:
            c = input('Number from 1-' + size + " of the URL you want to open: ")
            try:
                    c = int(c)
            except:
                    c = 100000
        selected_url = json_stuff[c]

        # Do stuff with it.
        channel_name = selected_url["channel"]
        channel_ID = selected_url["channel_claim_id"]

        claim_ID = selected_url["claimId"]
        url = str(librarian_instance + "api/comments?claim_id=" + claim_ID + "&channel_id=" + channel_ID + "&channel_name=" + channel_name + "&page=1&page_size=15")

        comments = requests.get(url)
        json_comments = json.loads(comments.text)
        for i, x in enumerate(json_comments["comments"]):
            if x["Channel"]["Name"] == '':
                print(i, bright_cyan+"DELETED USER"+norm+"\n"+x["Comment"])
            else:
                print(i, bright_cyan+x["Channel"]["Name"]+norm+"\n"+x["Comment"])
        print(bright_cyan+"DESCRIPTION:\n"+norm+json_stuff[c]["description"])
        url = librarian_instance + selected_url["channel"] + "/" + selected_url["name"]
        print("\n"+url)
        os.system(command + url)
        quit()
    elif sys.argv[1] == "-p":
        try:
            query = sys.argv[2]
        except:
            query = input("Searching for: ")
            query = str(query)
        size = str(19)
        pipedapi_search = pipedapi_instance + "search?q=" + query + "&filter=videos"
        data = requests.get(pipedapi_search)
        json_stuff = json.loads(data.text)
        for i, vid in enumerate(json_stuff["items"]):
            print(i, colora+vid["title"]+norm+"\n"+colorb+vid["uploaderName"]+norm+"\n"+bright_cyan+piped_instance[:-1]+vid["url"]+norm)

        c = 100000
        while not c >= 0 or not c <= 19:
            c = input("Number from 1-" + size + " of the URL you want to open: ")
            try:
                    c = int(c)
            except:
                    c = 100000

        videoId = json_stuff["items"][c]["url"]
        videoId = str(videoId)
        videoId = videoId.replace("/watch?v=", "")
        comments = pipedapi_instance + "comments/" + videoId
        data_comment = requests.get(comments)
        json_comment = json.loads(data_comment.text)
        for i, comment in enumerate(json_comment["comments"]):
            print(i, colora+bold+"@"+comment["author"]+norm, comment["commentedTime"]+norm+"\n"+colorb+comment["commentText"]+norm)

        selected_url = piped_instance + videoId
        print("\n"+colora+"DESCRIPTION:\n"+norm+json_stuff["items"][c]["shortDescription"])
        print("\n"+selected_url)
        os.system(command + selected_url)
        quit()
    elif sys.argv[1] == "-h":
        print('''
Command:
python vids.py <arg>
After doing this you will be prompted to make a search
If you want you can make the search in the command by doing
python vids.py <arg> "search"

LBRY network: arg = -l
-l for lighthouse (searching), librarian api (comments)

PeerTube: arg = -pt
-pt for sepia (searching), instance's API (comments) 

Invidious a proxy for YouTube: arg = -i
-i instance's api for comments and searching 

Piped a proxy for YouTube: arg = -p
-p instance's api for comments and searching 

At the top of the script there are a bunch of variables you can change
to set the instance you want. More explinations are there.
- command = "command on your system (include space at the end) "
- librarian_instance = "Librarian instance (include / at the end)"
- invidious_instance = "Invidious instance (include / at the end)"
- piped_instance = "Piped instance (include / at the end)"
- pipedapi_instance = "Piped instance API (include / at the end)"
''')
except:
    print('')
