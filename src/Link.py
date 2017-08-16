from Estimator import Estimator
from Histogram import Histogram
from Function import Logistic

class Link:

	def __init__(self, estimator, rate):
		self.state = 0
		self.error = 0
		self.weight = 0.5
		self.duration = 0
		self.last_fired = 0
	
		self.l_rate = rate
		self.estimator = estimator
	
		self.logistic = Logistic(1, 1, 1)
		

	def update(self, s, t):
		if s[0] == 1: 
			self.last_fired = t

		self.state = 0
		if self.last_fired != None:
			et = t-self.last_fired

			if self.duration-et <= 0:
				self.state = self.weight

			if s[1] == 1:
				self.error = abs(self.duration-et)			
				dw = self.logistic(self.error)-self.logistic.a/2

				self.weight -= dw * self.l_rate
				self.estimator.plot(t-self.last_fired)
				self.duration = self.estimator.peak()

				self.last_fired = None

	def __call__(self):
		return self.state
