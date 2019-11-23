import time
import random
from PIL import Image

def noxel():
	return (
		random.randrange(255),
		random.randrange(255),
		random.randrange(255),
		)

LINE = []

for i in range(512):
	LINE.append(noxel())

MATRIX = LINE*512

nixel = iter(MATRIX)

def noisefield():
	im = Image.new("RGB", (512, 512))
	for x in range(512):
		for y in range(512):
			im.putpixel((x, y), nixel.next())
	im.save("/<FILEPATH>/"+time.strftime('%Y%m%d%H%M%S')+".png")
	im.show()

"""
>>> noisefield()
"""
