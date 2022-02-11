# Script for searching YouTube through the invidious API, LBRY through
# lighthouse API and peertube through the SepiaSearch API. Played with
# mpv
import requests
import json
import os
import sys

print('''
/-------------------------------\\
|             vids              |
\\-------------------------------/
''')

# Use either a browser or mpv
command = "mpv "
bold = "\033[01m"
norm = "\033[00m"
bright_cyan = "\033[46m"
colora = "\033[45m"
colorb = "\033[44m"

try:
    if sys.argv[1] == "-i":
        invidious_instance = "https://invidio.xamh.de/"
        try:
            query = sys.argv[2]
        except:
            query = input("Searching for: ")
            query = str(query)
        size = str(19)
        invidious_search = invidious_instance + "api/v1/search?q=" + query
        wol_api = "https://scrap.madiator.com/api/get-lbry-video?url="

        data = requests.get(invidious_search)
        json_stuff = json.loads(data.text)
        for i, vid in enumerate(json_stuff):
            print(i, colora+vid["title"]+norm+"\n"+colorb+vid["author"]+norm+"\n"+bright_cyan+vid["videoId"]+norm)

        c = 100000
        while not c >= 0 or not c <= 19:
            c = input('Number from 1-' + size + " of the URL you want to open: ")
            try:
                    c = int(c)
            except:
                    c = 100000
        # wol-api check
        lbry_check = requests.get(wol_api + json_stuff[c]["videoId"])
        lbry_check = json.loads(lbry_check.text)
        # For now using odysee because yt-dlp doesn't support librarian
        librarian_instance = "https://odysee.com/"

        if lbry_check["lbryurl"] == None:
            # Using youtube.com since yt-dlp on any given invidious url redirects to youtube.com anyways.
            selected_url = "https://youtube.com/watch?v=" + json_stuff[c]["videoId"]
        else:
            print("Playing with LBRY!")
            selected_url = librarian_instance + lbry_check["lbryurl"]
            selected_url = selected_url.replace("#", ":")
        comments = invidious_instance + "/api/v1/comments/" + json_stuff[c]["videoId"]
        data_comment = requests.get(comments)
        json_comment = json.loads(data_comment.text)
        if "error" in json_comment:
            print("could not fetch comments")
        else:
            for i, comment in enumerate(json_comment["comments"]):
                print(i, colora+comment["author"]+norm+"\n"+colorb+comment["content"]+norm)

        # Do stuff with it.
        os.system(command + selected_url)
        quit()

    elif sys.argv[1] == "-p":
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

        selected_url = json_stuff["data"][c]["url"]
        comments = "https://" + json_stuff["data"][c]["account"]["host"] + "/api/v1/videos/" + json_stuff["data"][c]["uuid"] + "/comment-threads/"
        data_comment = requests.get(comments)
        json_comment = json.loads(data_comment.text)
        # PRINT COMMENTS!
        for i, comment in enumerate(json_comment["data"]):
            # Sometimes peertube likes to give nonsese json
            if comment["account"] == None:
                print(i, "No Account Data")

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
                        print(i, "No Account Data")
                    # This prints out the first reply.
                    else:
                        print(" " + str(i) + " " + colora+reply["comment"]["account"]["displayName"]+norm+"\n "+colorb+reply["comment"]["text"]+norm)

            # This is the final thing, the comment has no replys so it just
            # prints it as a comment.
            else:
                print(i, colora+comment["account"]["displayName"]+norm+"\n"+colorb+comment["text"]+norm)

        os.system(command + selected_url)

    elif sys.argv[1] == "-l":
        try:
            query = sys.argv[2]
        except:
            query = input("Searching for: ")
            query = str(query)
        size = str(30)
        search = 'https://lighthouse.lbry.com/search?s=' + query + '&include=channel,channel_claim_id,title&size=' + size
        lbry = "https://lbry.ix.tc/"

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
        url = str(lbry + "api/comments?claim_id=" + claim_ID + "&channel_id=" + channel_ID + "&channel_name=" + channel_name + "&page=1&page_size=15")

        comments = requests.get(url)
        json_comments = json.loads(comments.text)
        for i, x in enumerate(json_comments["comments"]):
            print(i, bright_cyan+x["Channel"]["Name"]+norm+"\n"+x["Comment"])

        url = "https://odysee.com/" + selected_url["channel"] + "/" + selected_url["name"]
        os.system(command + url)
        quit()
    elif sys.argv[1] == "-h":
        print('''
Command:
python vids.py <arg>
After doing this you will be prompted to make a search

If you want you can make the search in the command by doing
python vids.py <arg> "search"

-l for lighthouse (LBRY network)
-p for sepia (Peertube)
-i for invidious) (YouTube) 
NOTE: All youtube links will be checked with the Watch on LBRY API. If
the video is available on the lbry network, the youtube search result
will be opened in a odysee.com link.
''')
except:
    print('')
