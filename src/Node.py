from Estimator import Estimator
from Histogram import Histogram

class Node:

	def __init__(self, estimator=None):
		self.state = 0
		self.threshold = 0
		self.estimator = estimator
	def update(self, s):
		x = 0
		for i in s: 
			x += i
		
		y = 0
		if x > self.threshold: 
			y = 1

		if x != float('NaN') and x != float('inf'):
			self.estimator.plot(round(x*10))
		self.threshold = (self.estimator.peak())/10
		
		self.state = y

	def __call__(self):
		return self.state

