#!/usr/bin/env python
import os

for f in os.listdir():
    os.system(f'ffmpeg -i "{f}" -vcodec libx265 -crf 28 "small_{f}"')
    os.remove(f)
    os.rename(f"small_{f}",f)
