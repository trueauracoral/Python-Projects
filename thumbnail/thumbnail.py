# This is a script for me to generate video thumbnails for none video publications. I am way to lazy to create thumbnails so this just does it automaticly.

# Python image processing imports. Handling text and other things.
from PIL import Image, ImageDraw, ImageFont
# This if for text wrapping. Using \n isn't supported in PIL text stuff.
import textwrap

# Image open and draw
image = Image.open("background.png")
draw = ImageDraw.Draw(image)

# Text
text = input('Text: ')
textwrapped = textwrap.wrap(text, width=30)
dubai = ImageFont.truetype("ReemKufi-Regular.ttf", 100)
draw.text((400,400), '\n'.join(textwrapped), font=dubai, fill="black")

# I do some manipulation on the text variable so I get a nicer file name.
filename = text.replace(' ', '-')+".png"
image.save(filename, "PNG")
image.show()
