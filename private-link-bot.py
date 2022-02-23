"""
A detector of twitter, reddit and youtube links that will then print out safer sites that the user can use.

PROBLEMS:
- Annoying
- Not hosted reliably
"""

from matrix_bot_api.matrix_bot_api import MatrixBotAPI
from matrix_bot_api.mregex_handler import MRegexHandler
from matrix_bot_api.mcommand_handler import MCommandHandler

# Global variables
USERNAME = ""  # Bot's username
PASSWORD = ""  # Bot's password
SERVER = ""  # Matrix server URL


def youtube_callback(room, event):
    message = event["content"]["body"].split("/")
    room.send_text("Hi, " + event['sender'] + " here is a invidious link of the YouTube link you just sent:\nhttps://invidio.xamh.de/"+message[3])

def twitter_callback(room, event):
    message = event["content"]["body"]
    room.send_text("Hi, " + event['sender'] + " here is a nitter link of the Twitter link you just sent:\n"+message.replace("twitter.com","nitter.net"))

def reddit_callback(room, event):
    message = event["content"]["body"]
    room.send_text("Hi, " + event['sender'] + " here is a teddit link of the Reddit link you just sent:\n"+message.replace("reddit.com","teddit.net"))

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

    bot.start_polling()
    # Infinitely read stdin to stall main thread while the bot runs in other threads
    while True:
        input()


if __name__ == "__main__":
    main()
