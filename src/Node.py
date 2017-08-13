class Node:

	def __init__(self, t):
		self.t = t

	def update(self, s):
		x = 0
		for i in s: 
			x += i
		
		if x <= self.t: 
			return 1
		
		return 0
