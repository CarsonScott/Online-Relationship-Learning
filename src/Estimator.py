from Histogram import *
from Function import Gaussian, Logistic
from math import sqrt 

class Estimator:

	def __init__(self, histogram=None):
		self.space = histogram
		self.growth = Gaussian()
		self.decay = Logistic()

		self.g_rate = 0.007
		self.d_rate = 0.003

	def setspace(self, histogram):
		self.space = histogram

	def setgrowth(self, height, std_dev):
		self.growth.setparams(height, None, std_dev)

	def setdecay(self, height, gradient):
		self.decay.setparams(height, 0, gradient)
		self.decay.reflect()

	def plot(self, x):
		self.growth.b = x
		kernel = self.growth.c
		size = self.space.width

		for i in range(x-kernel, x+kernel):
			if i in range(0, size):
				self.space.plot(i, self.growth(i) * self.g_rate)

		for i in range(len(self.space.bins)):
			b = self.space.bins[i]
			if b > 0:

				db = self.decay(b) * self.d_rate
				b -= db
			if b < 0: b = 0

			self.space.bins[i] = b

	def __call__(self):
		return self.space.bins

	def peak(self):
		p = 0
		for i in range(len(self.space.bins)):
			if self.space.bins[i] > self.space.bins[p]:
				p = i
		return p
		
	def convert(self):
		m = 0
		p = 0
		c = 0
		for i in self.space.bins:
			v = self.space.bins[p]
			m += i
			if i > v: 
				p = c
			c += 1
		
		m /= c
		h = self.space.bins[p]

		l = h
		for i in range(p, -1, -1):
			f = self.space.bins[i]/h
			if f < h*0.01 or i == 0: 
				l = i
				break

		u = h
		for i in range(p, c):
			f = self.space.bins[i]/h
			if f < h*0.01 or i == c: 
				u = i
				break

		return (p, l, u)
