# Previewer script for LF/ranger etc written in python instead of
# shell script
#
# Most of the script is using the output from ffprobe which I think
# gets bundled with ffmpeg. Probably using mediainfo is more
# readable. I don't know how I can highlight code or something...
import subprocess
import sys
# This stupidly long list I got from Brodie Robertson's lfrc in his
# dotfiles repo.
media = [".bmp",".jpg",".jpeg",".png",".xpm",".wav",".mp3",".flac",".m4a",".wma",".ape",".ac3",".og[agx]",".spx",".opus",".as[fx]",".flac",".avi",".mp4",".wmv",".dat",".3gp",".ogv",".mkv",".mpg",".mpeg",".vob",".fl[icv]",".m2v",".mov",".webm",".ts",".mts",".m4v",".r[am]",".qt",".divx"]

file = sys.argv[1]
extension = "."+file.split(".")[1]
if extension in media:
    print("YAY")
    command = f"ffprobe -v quiet -show_format -show_streams \"{file}\""
    print(subprocess.getoutput(command))
else:
    with open(file) as f:
        print(f.read())
