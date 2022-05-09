import os
from pathlib import Path

folder = "C:\\SGZ_Pro\\"
files = os.listdir(folder)
def list():
    print(os.path.curdir())
    for i, file in enumerate(files):
        print(i, file)
list()
new = []
if os.path.isfile(folder+files[filepath]):
    print("FILE")
elif os.path.isdir(folder+files[filepath]):
    print("DIR")
    files = os.listdir(folder+files[filepath])
    list()
    filepath = int(input(":"))
#paths = sorted(Path(folder+dirs[dirpath]).iterdir(), key=os.path.getmtime)
