# Importing the PIL library
from PIL import Image
from PIL import ImageDraw

# Open an Image
img = Image.open('car.png')

# Call draw Method to add 2D graphis in an image
I1 = ImageDraw.Draw(img)

# Prompt the user for the text
text = input("Text:")

# Add Text to an image
I1.text(22, 32, text, fill="black")

# Display edited image
img.show()

# Save the edited image
img.save("car2.png")
