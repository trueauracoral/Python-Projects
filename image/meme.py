from PIL import Image, ImageDraw, ImageFont
import textwrap
import os
import pyperclip

toptext = input('top: ')
toptext = '\n'.join(textwrap.wrap(toptext, width=20))
bottomtext = input("bottom: ")
bottomtext = '\n'.join(textwrap.wrap(bottomtext, width=20))
image = Image.open("kmart.png")
draw = ImageDraw.Draw(image)
dubai = ImageFont.truetype("ReemKufi-Regular.ttf", 100)

W, H = (1920,1080)
wt, ht = draw.textsize(toptext, font=dubai)
wb, hb = draw.textsize(bottomtext, font=dubai)
shadowcolor = "#161616"
draw.text(((W-wt)/2,100), toptext, font=dubai, fill="#ffffff")
draw.text(((W-wb)/2,800), bottomtext, font=dubai, fill="#ffffff")

image.save("meme.png", "PNG")
image.show()
