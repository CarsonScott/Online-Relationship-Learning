from Estimator import Estimator
from Histogram import Histogram

class Node:

	def __init__(self, estimator):
		self.threshold = 0
		self.estimator = estimator

	def update(self, s):
		x = 0
		for i in s: 
			x += i
		
		y = 0
		if x >= self.threshold: 
			y = 1

		self.estimator.plot(round(x*10))
		self.threshold = self.estimator.peak()/10
		
		return y

