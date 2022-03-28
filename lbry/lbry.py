import requests
import json
import os
import subprocess
import sys
import re
import platform
import time
import tempfile

bold="\033[01m"
norm="\033[00m"
bright_cyan="\033[45m"
lbrynet = "lbrynet"
downloader = "yt-dlp"
url = "https://invidio.xamh.de/channel/UCo8bcnLyZH8tBIH9V1mLgqQ"

def mini_help():
    print('''An incorrect or no argument was passed.
+---------------+---------------+-----------------+
|Short options: | Long options: |     Meaning:    |
+---------------+---------------+-----------------+
|   -s          | --search      | Search LBRY     |
|   -y          | --yt          | YT to LBRY      |
|   -mu         | --massupload  | Upload directory|
|   -u          | --upload      | Upload file     |
|   -c          | --convert     | LBC to USD      |
|   -h          | --help        | Full Help       |
+---------------+---------------+-----------------+''')

if len(sys.argv) == 1:
    mini_help()

elif sys.argv[1] == "--search" or sys.argv[1] == "-s":
    query = input("Searching for: ")
    query = str(query)
    size = str(30)
    search = 'https://lighthouse.lbry.com/search?s=' + query + '&include=channel,channel_claim_id,title&size=' + size
    lbry = "https://lbry.ix.tc/"
    command = "C:\\SGZ_Pro\\z-apps_drivers\\mpv\\mpv.exe "

    data = requests.get(search)
    json_stuff = json.loads(data.text)

    for i, x in enumerate(json_stuff):
        pre = "lbry://"
        if x["channel"]:
            pre += x["channel"] + "/"
        url = pre + x["name"]
        print(i, bright_cyan+x["title"]+norm+"\n"+url)

    c = 100000
    while not c >= 0 or not c <= 29:
        c = input('Number from 1-' + size + " of the URL you want to open: ")
        try:
                c = int(c)
        except:
                c = 100000
    selected_url = json_stuff[c]

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
elif sys.argv[1] == "--convert" or sys.argv[1] == "-c":
    lbc = input("How much LBC? ")

    print(requests.get("https://rate.sx/" + lbc + "LBC").text.rstrip())
elif sys.argv[1] == "--upload" or sys.argv[1] == "-u":
    # Got from: https://notabug.org/jyamihud/FastLBRY-terminal/src/master/flbry/variables.py#L502
    licenses = [
# NAME , URL , COMMENT
["GNU General Public License Version 3 (or later)",
"https://www.gnu.org/licenses/gpl-3.0.html",
"Strong Copyleft. Recommended for Software."],
["GNU General Public License Version 3 (only)",
"https://www.gnu.org/licenses/gpl-3.0.html",
"Strong Copyleft."],
["GNU Free Documentation License",
"https://www.gnu.org/licenses/fdl-1.3.html",
"Strong Copyleft. Recommended for books."],
["Creative Commons Attribution-ShareAlike 4.0 International",
"https://creativecommons.org/licenses/by-sa/4.0/",
"Copylefted, Recommended for Art."],
["Creative Commons Attribution 4.0 International",
"https://creativecommons.org/licenses/by/4.0/",
"Non Copylefted, Free License."],
["Creative Commons Zero 1.0 International",
"https://creativecommons.org/publicdomain/zero/1.0/",
"Public Domain"],
["Creative Commons Attribution-NoDerivatives 4.0 International",
"https://creativecommons.org/licenses/by-nd/4.0/",
"Does not allow changes. Recommended for opinion pieces."]
]

    # Check that lbry sdk is running.
    if subprocess.getoutput(f"{lbrynet} version") == "Could not connect to daemon. Are you sure it's running?":
        print('It looks like lbrynet has not started yet. In another terminal window/tab do "lbrynet start" and rerun this script.')
        quit()

    # Channel
    channels = subprocess.getoutput(f"{lbrynet} channel list")
    json_stuff = json.loads(channels)
    for i, channel in enumerate(json_stuff["items"]):
        print(i, "|", channel["name"])

    c = 100000
    while not c >= 0 or not c <= i:
        c = input('Select a channel from 0-'+str(i)+': ')
        try:
                c = int(c)
        except:
                c = 100000
    channel = json_stuff["items"][c]["name"]

    print(f"Uploading to {channel}.\n---")

    # Title
    title = input("Title for the publication: ")

    # Url
    print("---\nPressing enter will make it the title just with removed special characters.")
    url = input("Custome lbry url name: ")
    if url == "":
        name = re.sub(r'[\W_]+','', str(title))

    # Bid
    try:
        print("---\nCould be costly to do a upload, press enter and bid will be 0.1")
        bid = str(input("Per upload, how much bid do you want? "))
    except:
        bid = str(0.1)

    # Description
    try:
        print("---\nPressing enter will make the publication not have a description")
        description = input("Description for publication: ")
        #description = description.replace("\n","\\n")
        description = description.replace('"','\\"')
        description = description.replace("'","\\'")
    except:
        description = ""

    # Thumbnail
    try:
        print("---\nIf you want, a thumbnail can be uploaded to lbry. It will have all atributes of the video just the lbry name will be plus 123. Press enter for no thumbnail.")
        thumbnail = input("Thumbnail file location: ")
    except:
        thumbnail = ""

    name_thumb = re.sub(r'[\W_]+','', str(title)) + str(123)

    # Publication
    print("---\nFinally we are at the last step!")
    publication = input("Publication file location: ")

    # License
    for i, license in enumerate(licenses):
        print(i,*licenses[i],sep='\n')

    l = 100000
    while not l >= 0 or not l <= 7:
        l = input('Select a license from 0-7: ')
        try:
                l = int(l)
        except:
                l = 100000

    license = licenses[l][0]
    license_url = licenses[l][1]


    if thumbnail == "":
        print("---\nUploading puplication to LBRY!\n---")
        command = f'{lbrynet} publish --name={name} --bid={bid} --file_path="{publication}" --title="{title}" --description="{description}" --channel_name={channel} --license="{license}" --license_url="{license_url}"'
        os.system(command)
    else:
        print("\n---\nUploading thumbnail to LBRY!")
        thumbnail_command = f'{lbrynet} publish --name={name_thumb} --bid={bid} --file_path="{thumbnail}" --title="{title}" --description="{description}"'
        thumbnail_data = subprocess.getoutput(thumbnail_command)
        json_stuff = json.loads(thumbnail_data)
        thumbnail_url = json_stuff["outputs"][0]["permanent_url"].replace("lbry:/","https://spee.ch")
        print("\n---\nUploading puplication to LBRY!\n---")
        command = f'{lbrynet} publish --name={name} --bid={bid} --file_path="{publication}" --title="{title}" --description="{description}" --channel_name={channel} --thumbnail="{thumbnail_url}" --license="{license}" --license_url="{license_url}"'
        os.system(command)

    print("\n---\nLINK:\n---")
    print(f"https://spee.ch/{channel}/{name}")
    
elif sys.argv[1] == "--massupload" or sys.argv[1] == "-mu":
    files = os.listdir()
    if platform.system() == "Windows":
        slash = "\\"
    else:
        slash = "/"
    file_path = os.getcwd() + slash

    if subprocess.getoutput(f"{lbrynet} version") == "Could not connect to daemon. Are you sure it's running?":
        print('It looks like lbrynet has not started yet. In another terminal window/tab do "lbrynet start" and rerun this script.')
        quit()

    channels = subprocess.getoutput(f"{lbrynet} channel list")
    json_stuff = json.loads(channels)
    for i, channel in enumerate(json_stuff["items"]):
        print(i, "|", channel["name"])

    c = 100000
    while not c >= 0 or not c <= i:
        c = input('Select a channel from 0-'+str(i)+': ')
        try:
                c = int(c)
        except:
                c = 100000
    channel = json_stuff["items"][c]["name"]
    print(f"Mass uploading to {channel}.")

    try:
        print("---\nCould be costly to do a mass upload, press enter and bid will be 0.1")
        bid = str(input("Per upload, how much bid do you want? "))
    except:
        bid = str(0.1)

    #try:
    #    print('---\nDo you want a special description? Press enter and the description will be "mass upload"')
    #    description = input('Description for every upload: ')
    #except:
    #    description = "mass upload"

    for image in files:
        if sys.argv[0] in image:
            print("Not going to upload {sys.argv[0]}")
            pass
        else:
            os.system(f'{lbrynet} publish --name={image} --bid=0.1 --file_path="{file_path + image}" --title="{image}" --channel_name={channel}')
        time.sleep(30)

    for image in files:
        print(f"https://spee.ch/{channel}/{image}")

elif sys.argv[1] == "--notifications" or sys.argv[1] == "-n":
    with open('auth_token.json', 'r') as f:
        json_stuff = json.load(f)

    auth_token = json_stuff["auth_token"]

    notifications = requests.post("https://api.odysee.com/notification/list", data={"auth_token":auth_token}).json()

    #print(json.dumps(notifications, indent=4))

    for i in notifications["data"]:
        if i["is_read"] == "true":
            print("--")
            print(i["notification_parameters"]["device"]["title"])
            print(i["notification_parameters"]["device"]["target"])
            print(i["notification_parameters"]["device"]["text"])
        else:
            print("No new notifications!")
            break

elif sys.argv[1] == "--yt" or sys.argv[1] == "--y":
    temp_dir = tempfile.TemporaryDirectory().name

    url = url.split("/")
    pipedapi = f"https://pipedapi.kavin.rocks/channel/{url[4]}"
    data = requests.get(pipedapi)
    json_stuff = json.loads(data.text)
    id = str(json_stuff["relatedStreams"][0]["url"]).replace("/watch?v=","")
    video = requests.get("https://pipedapi.kavin.rocks/streams/"+id)
    video_json = json.loads(video.text)
    title = video_json["title"]
    name_thumb = re.sub(r'[\W_]+','', str(title)) + str(123)
    name = re.sub(r'[\W_]+','', str(title))

    if subprocess.getoutput(f"{lbrynet} version") == "Could not connect to daemon. Are you sure it's running?":
        print('It looks like lbrynet has not started yet. In another terminal window/tab do "lbrynet start" and rerun this script.')
        quit()

    channels = subprocess.getoutput(f"{lbrynet} channel list")
    json_stuff = json.loads(channels)
    for i, channel in enumerate(json_stuff["items"]):
        print(i, "|", channel["name"])

    c = 100000
    while not c >= 0 or not c <= i:
        c = input('Select a channel from 0-'+str(i)+': ')
        try:
                c = int(c)
        except:
                c = 100000
    channel = json_stuff["items"][c]["name"]
    print(f"Uploading to {channel}.")
    try:
        print("---\nCould be costly to do a upload, press enter and bid will be 0.1")
        bid = str(input("Per upload, how much bid do you want? "))
    except:
        bid = str(0.1)

    description = (f"""---
This is a LBRY mirror of of this video:
{title}
Original YT URL (THIS IS SPYWARE): https://youtube.com/watch?v={id}
---
{video_json["description"]}""")

    print(description)
    description = description.replace("\n","\\n")
    description = description.replace('"','\\"')
    description = description.replace("'","\\'")

    print("\n---\nYT download starting:")
    os.system(f"{downloader} https://youtube.com/watch?v={id}")

    print("\n---\nUploading thumbnail to LBRY!")
    thumbnail_data = requests.get(video_json["thumbnailUrl"])
    with open(temp_dir, 'wb') as f:
        f.write(thumbnail_data.content)

    thumbnail_command = f'{lbrynet} publish --name={name_thumb} --bid={bid} --file_path="{temp_dir}" --title="{title}" --description="{description}"'
    #os.system(thumbnail_command)
    thumbnail_data = subprocess.getoutput(thumbnail_command)
    json_stuff = json.loads(thumbnail_data)
    thumbnail_url = json_stuff["outputs"][0]["permanent_url"].replace("lbry:/","https://spee.ch")
    print(thumbnail_url)

    if platform.system() == "Windows":
        slash = "\\"
    else:
        slash = "/"
    cwd = os.getcwd()

    print("\n---\nUploading video to LBRY!\n---")
    command = f'{lbrynet} publish --name={name} --bid={bid} --file_path="{cwd}{slash}{title} [{id}].mp4" --title="{title}" --description="{description}" --channel_name={channel} --thumbnail="{thumbnail_url}"'
    os.system(command)

    print("\n---\nLINK:\n---")
    print(f"https://spee.ch/{channel}/{name}")
elif sys.argv[1] == "-h" or sys.argv[1] == "--help":
    print('''Command:
python lbry.py <arg>

Search the LBRY network:
-s or --search for lighthouse (searching), librarian api (comments)

Convert LBC to USD
-c or --convert for rate.sx:

Mass upload:
-mu or --massupload using the LBRY sdk to mass upload all files in directory to LBRY.

Upload:
-u or --upload using the LBRY sdk to upload a file to LBRY.

Upload youtube to LBRY:
-y or --yt using the LBRY sdk and yt-dlp to upload new video from a youtube channel to LBRY.''')
else:
    mini_help()
    quit()
