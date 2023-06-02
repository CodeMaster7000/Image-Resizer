import traceback
from PIL import Image
def resize():
	filePath = 'example.jpg'
	ratio = 0.5
	image = Image.open(filePath)
	width = image.size[0]
	height = image.size[1]
	newWidth = int(round(width * ratio))
	newHeight = int(round(height * ratio))
	newImage = image.resize((newWidth, newHeight), Image.ANTIALIAS)
	newImage.format = image.format
	newImage.save(filePath)

if __name__ == '__main__':
	try:
		resize()
	except Exception as e:
		traceback.print_exc(e)
		raw_input()
