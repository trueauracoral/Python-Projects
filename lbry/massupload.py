import os
import re
import platform

lbrynet = "lbrynet"
files = os.listdir()
if platform.system() == "Windows":
    slash = "\\"
else:
    slash = "/"
file_path = os.getcwd() + slash

for image in files:
    print(image)
    os.system(f'{lbrynet} publish --name={image} --bid=0.1 --file_path="{file_path + image}" --title="{image}" --description="mass art upload for TrueAuraCoraL :)" --channel_name=@TrueAuraCoralPublishesImages')
for image in files:
    print(f"https://spee.ch/@TrueAuraCoralPublishesImages/{image}")
