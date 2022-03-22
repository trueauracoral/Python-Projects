import os
import re

lbrynet = "lbrynet"
files = os.listdir()
file_path = os.getcwd() + "\\"

#for image in files:
#    print(image)
#    os.system(f'{lbrynet} publish --name={image} --bid=0.1 --file_path="{file_path + image}" --title="{image}" --description="mass art upload for TrueAuraCoraL :)" --channel_name=@TrueAuraCoralPublishesImages')
for image in files:
    print(f"https://spee.ch/@TrueAuraCoralPublishesImages/{image}")
