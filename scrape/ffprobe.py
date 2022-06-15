#!/usr/bin/env python
import os
import subprocess
import json

file = input("File: ")
command = f"ffprobe -v quiet -print_format json -show_format -show_streams \"{file}\""
data = subprocess.getoutput(command)
print(data)
data = json.loads(data)

print(data["streams"][0]["codec_name"])
print(data["streams"][0]["codec_type"])
print(f'{data["streams"][0]["width"]}x{data["streams"][0]["height"]}')
