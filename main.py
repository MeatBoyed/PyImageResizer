from PIL import Image
import glob

for filename in glob.glob("./Photos/*.jpg"):

	image = Image.open(filename)
	newImage = image.resize((300, 270))
	newImage.save(f"{filename}New.jpg")
