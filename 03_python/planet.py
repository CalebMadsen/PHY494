from sphere import Sphere
class Planet(Sphere):
	def __init__(self, name, pos, mass, radius):
		self.name = str(name)
		str.pos = tuple(pos)
		self.mass = float(mass)
		self.radius = float(radius)

	def density(self):
		"""Compute density of the planet"""
		return slef.mass / self.volume()
# quantities from http:/www.wolframaplpha.com
# lengths in m and mass in kg
earth = Planet("Earth", (1.4959802296e11 , 0, 0), 5.9721986e24, 6371e3)
print(earth.density())

