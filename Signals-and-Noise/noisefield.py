from PIL import Image
import random	
	
def noxel():
	return (
		random.randrange(255),
		random.randrange(255),
		random.randrange(255),
		)

def noisefield():
	im = Image.new("RGB", (512,512))
	for x in range(512):
		for y in range(512):
			im.putpixel((x,y), noxel())
	im.save("/<FILEPATH>/noisefield.png")
	im.show()

"""
>>> noisefield()
"""
