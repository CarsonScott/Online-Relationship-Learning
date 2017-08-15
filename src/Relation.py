from Function import gaussian
from time import clock

class Relation:

	def __init__(self, f, l):
		self.delay  = 0.5
		self.range  = 0.5
		self.weight = 1.0

		self.f = f
		self.l = l

		self.ff = None
		self.lf = None

	def reset(self):
		self.ff = None
		self.lf = None

	def valid(self):
		f = self.ff
		l = self.lf
		return None not in (f,l)
	
	def fitness(self, x):
		a = self.weight
		b = self.delay
		c = self.range

		return gaussian(x, a, b, c)

	def update(self, fs, ls, t):
		if fs != 0: self.ff = t
		if ls != 0: self.lf = t
		y = None

		if self.valid():
			x = self.lf-self.ff
			y = self.fitness(x)		
			self.reset()

		return y


r = Relation(0, 1)

for i in range(10):
	x = 0
	if i == 0:
		x = r.update(1, 0, i)
	elif i == 5:
		x = r.update(0, 1, i)
	else:
		x = r.update(0, 0, i)
	print(x)