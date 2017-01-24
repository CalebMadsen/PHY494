import numpy as np
class Sphere:
	"""A simple sphere."""
	
	def __init__(self, pos, radius=1):
		self.pos = tuple(pos)
		self.radius = float(radius)

	def volume(self):
		return 4/3 *np.pi * self.radius**3

	def translate(self, t):
		self.pos = tuple(xi + ti for xi, ti in zip(self.pos, t))

