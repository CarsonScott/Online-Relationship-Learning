def norm(x):
	if x != 0: return x/abs(x) 
	return 0

def sigmoid(x):
	return x/(1+abs(x))

class Network:

	def __init__(self, n):
		self.states = [0  for i in range(n)]
		self.thresh = [0  for i in range(n)]
		self.inputs = [[] for i in range(n)]
		
		self.nDelta = [0  for i in range(n)]
		self.nAccel = [0  for i in range(n)]
		self.nError = [0  for i in range(n)]

		self.links = []
		self.delay = []
		self.pairs = []
		self.times = []
		self.ready = []

		self.lDelta = []
		self.lAccel = []
		self.lError = []
		
		self.x = []
		self.y = []
		self.init()

	def init(self, lr=None, dr=None):
		self.learn_rate = lr
		self.decay_rate = dr

	def connect(self, i, f):		
		self.links.append(0)
		self.delay.append(0)
		self.lError.append(0)
		self.lDelta.append(0)
		self.lAccel.append(0)
		self.ready.append(0)

		l = len(self.links)-1
		self.inputs[f].append(l)
		self.pairs.append([i, f])
		self.times.append([0, 0])

	def set_x(self, x):
		self.x = x

	def set_y(self, y):
		self. y = y

	def update_links(self, t):
		
		for r in range(len(self.pairs)):
			if self.links[r]:
				self.links[r] = 0
				self.lError[r] = 0
				self.lDelta[r] = 0

			if self.lAccel[r] > 0: 
				da = sigmoid(self.lAccel[r])*self.decay_rate
				self.lAccel[r] -= da
			i = self.pairs[r][0]
			f = self.pairs[r][1]

			si = self.states[i]
			sf = self.states[f]
			if si: self.times[r][0] = t
			if sf: self.times[r][1] = t
			
			ti = self.times[r][0]
			tf = self.times[r][1]
			pt = self.delay[r]
			dt = tf-ti


			if dt < 0: 
				self.ready[r] = 1

			elif self.ready[r]:
				dp = dt-pt
				pe = 0.5*dp**2
				self.lDelta[r] = dp				
				self.lError[r] = pe 

				da = self.lDelta[r]
				dd = self.lAccel[r] + da
				a = self.lAccel[r] + sigmoid(da)*self.learn_rate
				d = self.delay[r] + dd*self.learn_rate

				self.lAccel[r] = a
				self.delay[r] = d
				self.links[r] = 1				
				self.ready[r] = 0

	def update_nodes(self):

		for n in range(len(self.inputs)):
			if self.states[n]: 
				self.states[n] = 0
				self.nError[n] = 0
				self.nDelta[n] = 0

			if self.nAccel[n] > 0:
				dt = sigmoid(self.nAccel[n])*self.decay_rate
				self.thresh[n] -= dt

			xs = 0
			xt = self.thresh[n]
			
			for r in range(len(self.inputs[n])):
				xs += self.links[self.inputs[n][r]]

			dp = xs-xt
			if dp > 0:
				pe = 0.5*dp**2
				self.nDelta[n] = dp
				self.nError[n] = pe

				da = self.nDelta[n]
				dt = self.nAccel[n] + da
				a = self.nAccel[n] + sigmoid(da)*self.learn_rate
				t = self.thresh[n] + dt*self.learn_rate

				self.nAccel[n] = a
				self.thresh[n] = t
				self.states[n] = 1

	def update(self, x, t):
		for n in range(len(self.x)):
			self.states[self.x[n]] = x[n]

		self.update_links(t)
		self.update_nodes()

		y = []
		for n in range(len(self.y)):
			y.append(self.states[self.y[n]])
		return y
