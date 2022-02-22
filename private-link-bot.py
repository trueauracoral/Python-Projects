"""
Hi I am a matrix bot for printing out invidious links.
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
    room.send_text("Hi, " + event['sender'] + " Please use invidious or piped or viewtube. YouTube Sucks.\n\nHere is a invidious link of the YouTube link you just sent:\nhttps://invidio.xamh.de/"+message[3])

def echo_callback(room, event):
    args = event['content']['body'].split()
    args.pop(0)

    room.send_text(' '.join(args))

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

    # Add a regex handler waiting for the echo command
    echo_handler = MCommandHandler("echo", echo_callback)
    bot.add_handler(echo_handler)

    bot.start_polling()
    # Infinitely read stdin to stall main thread while the bot runs in other threads
    while True:
        input()


if __name__ == "__main__":
    main()
