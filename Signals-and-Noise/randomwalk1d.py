import random
import matplotlib.pylab as plt
import numpy as np


def random_walk(n):
	x = 0
	c = [x]
	for i in range(n):
		prob = random.random()
		if prob > 0.5:
			x = x + 1
		elif prob < 0.5:
			x = x - 1
		c.append(x)
	return c


numberOfSteps = 100
walk = random_walk(numberOfSteps)

n = np.arange(numberOfSteps+1)

plt.plot(n, walk, 'r-')
plt.plot(n, walk, 'bo')
plt.xlabel('Time (n)')
plt.ylabel('Position (x)')
plt.show()
