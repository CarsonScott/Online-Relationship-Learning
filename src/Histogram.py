from math import floor

class Histogram:

	def __init__(self, width=None, bins=None, max=None):
		self.setparams(width, bins, max)

	def setparams(self, width=None, bins=None, max=None):
		self.width = width
		self.max = max
		self.bins = [0 for i in range(bins)]

	def plot(self, x, v):
		i = int(x)
		self.bins[i] += v

		if self.max != None:
			self.limit(i)

	def limit(self, i):
		if self.bins[i] > self.max:
			p = self.bins[i]
			for b in range(len(self.bins)):
				self.bins[b] = self.bins[b]*self.max/p
		