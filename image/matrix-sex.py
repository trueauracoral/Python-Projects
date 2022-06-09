# Some code I got from:
# https://github.com/rebane2001/txnor-server/blob/mane/sex.py
from PIL import Image, ImageFont, ImageDraw, ImageEnhance
import os

image="C:\SGZ_Pro\Hobbys\Media\memes\pepes\\55.png"
base_img ="C:\\SGZ_Pro\\Hobbys\\Media\\sex_base.png"
font="C:\\SGZ_Pro\\Hobbys\\Media\\impact.ttf"
img = Image.open(image).resize((350, 185)).convert("RGB")

draw = ImageDraw.Draw(img)
font = ImageFont.truetype("impact.ttf", 32)
draw.text((350 / 2, 0), "WTF MATRIX SEX", (255, 255, 255), font=font, anchor="ma", stroke_width=2,
          stroke_fill=(0, 0, 0))
draw.text((350 / 2, 185), "??? WTF ??? SEX ???", (255, 255, 255), font=font, anchor="md", stroke_width=2,
stroke_fill=(0, 0, 0))

img.save("output.png", "JPEG",quality=10)

base = Image.open(base_img)
base.paste(img,(5,100))
base.save("output.png","PNG",quality=10)