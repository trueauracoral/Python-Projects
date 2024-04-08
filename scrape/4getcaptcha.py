from PIL import Image

def main():
    birds = Image.open("captcha3.jpeg") # birds
    fumoPlushies = Image.open("captcha2.jpeg") # fumo plushies
    minecraft = Image.open("captcha.jpeg") # minecraft

    #getText(birds)
    getImages(birds)

def getText(image):
    textMargin = (0, 0, 400, 27)
    text = image.crop(textMargin)
    text.save("text.jpeg")
    text.show()

def getImages(image):
    imageMargin = (0, 27, 400, 427)
    images = image.crop(imageMargin)
    images.save("images.jpeg")
    images.show()
    # All images are 100x100
    width = 100
    height = 100
    imageGrid = []
    for row in list(range(4)):
        imageRow = []
        for cell in list(range(4)):
            #imageRow += [f"{cell * width}, {row * height}, {(cell + 1) * width}, {(row + 1) * height}"]
            imageRow += [images.crop((cell * width, row * height, (cell + 1) * width, (row + 1) * height))]
        imageGrid += [imageRow]
    print(imageGrid)

    for i, image in enumerate(imageGrid):
        for j, img in enumerate(image):
            img.save(f"img{i}-{j}.jpeg")

if __name__ == "__main__":
    main()