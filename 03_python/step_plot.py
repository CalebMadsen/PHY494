# heaviside step function

def heaviside(x):
	"""Heaviside step function"""

	theta = None
	if x < 0:
		theta = 0.
	elif x == 0:
		theta = 0.5
	else:
		theta = 1.

	return theta

xvalues = []
h = .5
xmin, xmax = -4, 4
x = xmin
while x <= xmax:
	xvalues.append(x)
	x += h

# print(xvalues)
theta = []
for x in xvalues:
	theta.append(heaviside(x))

print(xvalues)
print(theta)

