import os

# ffmpeg -ss 00 -i <VID> -t 55 -c copy out.mp4
video = input("Video: ")
starttime = input("Start time: ")
endtime = input("End time: ")
output = input("Output: ")
command = f"ffmpeg -ss {starttime} -i {video} -t {endtime} -c copy {output}"
os.system(command)
