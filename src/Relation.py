from Estimator import Estimator
from Histogram import Histogram

class Relation:

	def __init__(self, estimator):
		self.duration = 0
		self.last_fired = 0
		self.estimator = estimator

	def update(self, s, t):
		if s[0] == 1:
			self.last_fired = t

		y = 0
		if self.last_fired != None:
			if self.duration - (t-self.last_fired) <= 0:
				y = 1

		if s[1] == 1 and self.last_fired != None:
			self.estimator.plot(t-self.last_fired)
			self.duration = self.estimator.peak()
			self.last_fired = None

		return y
