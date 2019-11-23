import time
import random
from PIL import Image

def noisefield():
	im = Image.new("L", (512, 512))
	for x in range(512):
		for y in range(512):
			im.putpixel((x, y), random.choice([0,255]))
	im.save(filepath+time.strftime('%Y%m%d%H%M%S')+".png")
	im.show()
