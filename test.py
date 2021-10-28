from PIL import Image

image = Image.open("./profile.jpg")

newImage = image.resize((123, 123))
newImage.save("./newProfile.jpg")

