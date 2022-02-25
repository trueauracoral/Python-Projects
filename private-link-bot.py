"""
At it's core a detector of twitter, reddit and youtube links that will then print out safer sites that the user can use.

PROBLEMS:
- Annoying
- Not hosted reliably
"""

from matrix_bot_api.matrix_bot_api import MatrixBotAPI
from matrix_bot_api.mregex_handler import MRegexHandler
from matrix_bot_api.mcommand_handler import MCommandHandler
import requests
import json
import re

# Global variables
USERNAME = ""  # Bot's username
PASSWORD = ""  # Bot's password
SERVER = ""  # Matrix server URL

def help_callback(room, event):
    room.send_text("""
fossbot is a matrixbot that can do multiple things:

- Detect sent youtube, reddit or twitter links and send back a message link with a proxy site such as: invidious, teddit and nitter.

Commands:
- fossbot-help
Print out this help message.
- fossbot-youtube <qeury>
Print out youtube search results as invidious links with title and channel information. Uses the invidious API
- fossbot-peertube <qeury>
Print out peertube search results as peertube instance links with title and channel information. Uses the sepiasearch API
- fossbot-lbry <query>
Print out LBRY search results as librarian links with title and channel information. Uses the lighthouse API
- fossbot-crypto <query>
Print out in USD values of crypto currencies. Uses the rate.sx API.
- fossbot-neow <query>
Print out the amount of neow coins a user on neow has.
- fossbot-wikipedia <query>
Print out wikipedia search result snippets of different articles.
""")
    print(event['sender']+"\nPosted:\n"+event["content"]["body"])

def wikipedia_callback(room, event):
    message = event["content"]["body"].replace("fossbot-wikipedia ","")
    query = message
    wikipedia_api = f"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch={query}&format=json"
    data = requests.get(wikipedia_api)
    json_stuff = json.loads(data.text)
    room.send_text(f"Searching for {query}")

    for index, post in enumerate(json_stuff["query"]["search"]):
        clean = re.compile('<.*?>')
        room.send_text(re.sub(clean, '', post["title"]+"\n"+post["snippet"]))
        if index == 2:
            break
    print(event['sender']+"\nPosted:\n"+event["content"]["body"])

def neow_callback(room, event):
    message = event["content"]["body"].replace("fossbot-neow ","")
    query = message
    neow_search = "https://neow.matthewevan.xyz/user/" + query + "/neowcoins.txt"
    data = requests.get(neow_search).text.rstrip()
    room.send_text(query + " has " + data + " coins")
    print(event['sender']+"\nPosted:\n"+event["content"]["body"])

def crypto_callback(room, event):
    message = event["content"]["body"].replace("fossbot-crypto ","")
    query = message
    ratesx_search = "https://rate.sx/" + query
    data = requests.get(ratesx_search).text.rstrip()
    room.send_text("In USD that's " + data)
    print(event['sender']+"\nPosted:\n"+event["content"]["body"])

def peertube_callback(room, event):
    message = event["content"]["body"].replace("fossbot-peertube ","")
    query = message
    peertube_search = "https://sepiasearch.org/api/v1/search/videos?search=" + query
    data = requests.get(peertube_search)
    json_stuff = json.loads(data.text)
    room.send_text("Searching PeerTube for: " + query)
    for index, vid in enumerate(json_stuff["data"]):
        room.send_text(vid["name"]+"\n"+vid["channel"]["displayName"]+"\n"+vid["url"])
        if index == 4:
            break
    print(event['sender']+"\nPosted:\n"+event["content"]["body"])

def invidious_callback(room, event):
    message = event["content"]["body"].replace("fossbot-youtube ","")
    query = message
    invidious_search = "https://invidio.xamh.de/api/v1/search?q=" + query
    data = requests.get(invidious_search)
    json_stuff = json.loads(data.text)
    room.send_text("Searching youtube for: " + query)
    for index, vid in enumerate(json_stuff):
        room.send_text(vid["title"]+"\n"+vid["author"]+"\n"+"https://invidio.xamh.de/watch?v="+vid["videoId"])
        if index == 4:
            break
    print(event['sender']+"\nPosted:\n"+event["content"]["body"])
def lbry_callback(room, event):
    size = str(5)
    message = event["content"]["body"].replace("fossbot-lbry ","")
    query = message
    search = 'https://lighthouse.lbry.com/search?s=' + query + '&include=channel,title,&size=' + size

    data = requests.get(search)
    json_stuff = json.loads(data.text)

    room.send_text("Searching for: " + query)
    for x in json_stuff:
        pre = "https://lbry.ix.tc/"
        if x["channel"]:
            pre += x["channel"] + "/"
        url = pre + x["name"]
        room.send_text(x["title"]+"\n"+url)
    print(event['sender']+"\nPosted:\n"+event["content"]["body"])

def youtube_callback(room, event):
    message = event["content"]["body"].split("/")
    room.send_text("Hi, " + event['sender'] + " here is a invidious link of the YouTube link you just sent:\nhttps://invidio.xamh.de/"+message[3])
    print(event['sender']+"\nPosted:\n"+event["content"]["body"])

def twitter_callback(room, event):
    message = event["content"]["body"]
    room.send_text("Hi, " + event['sender'] + " here is a nitter link of the Twitter link you just sent:\n"+message.replace("twitter.com","nitter.net"))
    print(event['sender']+"\nPosted:\n"+event["content"]["body"])

def reddit_callback(room, event):
    message = event["content"]["body"]
    room.send_text("Hi, " + event['sender'] + " here is a teddit link of the Reddit link you just sent:\n"+message.replace("reddit.com","teddit.net"))
    print(event['sender']+"\nPosted:\n"+event["content"]["body"])

def main():
    # Create an instance of the MatrixBotAPI
    bot = MatrixBotAPI(USERNAME, PASSWORD, SERVER)

    #youtube_com_handler = MRegexHandler("^((?:https?:)?//)?((?:www|m).)?((?:youtube(-nocookie)?.com|youtu.be))(/(?:[\w-]+?v=|embed/|v/)?)([\w-]+)(\S+)?$", youtube_callback)
    youtube_com_handler = MRegexHandler("https://youtube.com/", youtube_callback)
    bot.add_handler(youtube_com_handler)
    youtube_handler = MRegexHandler("https://youtu.be/", youtube_callback)
    bot.add_handler(youtube_handler)
    youtube_www_handler = MRegexHandler("https://www.youtube.com/", youtube_callback)
    bot.add_handler(youtube_www_handler)
    twitter_handler = MRegexHandler("https://twitter.com/", twitter_callback)
    bot.add_handler(twitter_handler)
    reddit_handler = MRegexHandler("https://reddit.com/", reddit_callback)
    bot.add_handler(reddit_handler)
    invidious_handler = MRegexHandler("^fossbot-youtube", invidious_callback)
    bot.add_handler(invidious_handler)
    lbry_handler = MRegexHandler("^fossbot-lbry", lbry_callback)
    bot.add_handler(lbry_handler)
    crypto_handler = MRegexHandler("^fossbot-crypto", crypto_callback)
    bot.add_handler(crypto_handler)
    neow_handler = MRegexHandler("^fossbot-neow", neow_callback)
    bot.add_handler(neow_handler)
    help_handler = MRegexHandler("^fossbot-help", help_callback)
    bot.add_handler(help_handler)
    peertube_handler = MRegexHandler("^fossbot-peertube", peertube_callback)
    bot.add_handler(peertube_handler)
    wikipedia_handler = MRegexHandler("^fossbot-wikipedia", wikipedia_callback)
    bot.add_handler(wikipedia_handler)

    bot.start_polling()
    # Infinitely read stdin to stall main thread while the bot runs in other threads
    while True:
        input()

if __name__ == "__main__":
    main()
