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
		self.links = []
		self.delay = []
		self.pairs = []
		self.times = []
		self.delta = []
		self.error = []
		self.ready = []
		self.accel = []
		self.x = []
		self.y = []
		self.init()

	def init(self, lr=None, dr=None):
		self.learn_rate = lr
		self.decay_rate = dr

	def connect(self, i, f):		
		self.links.append(0)
		self.delay.append(0)
		self.error.append(0)
		self.delta.append(0)
		self.ready.append(0)
		self.accel.append(0)

		l = len(self.links)
		self.inputs[f].append(l)
		self.pairs.append([i, f])
		self.times.append([0, 0])

	def set_x(self, x):
		self.x = x

	def set_y(self, y):
		self. y = y

	def update_links(self, t):
		
		for r in range(len(self.pairs)):
			DR = self.decay_rate

			if self.links[r]:
				self.links[r] = 0
				self.error[r] = 0
				self.delta[r] = 0
			if self.accel[r] > 0: 
				da = sigmoid(self.accel[r])*self.decay_rate
				self.accel[r] -= da
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
				self.delta[r] = dp				
				self.error[r] = pe 

				LR = self.learn_rate
				
				da = self.delta[r]
				dd = self.accel[r] + da
				a = self.accel[r] + sigmoid(da)*LR
				d = self.delay[r] + dd*LR

				self.accel[r] = a
				self.delay[r] = d
				self.links[r] = 1				
				self.ready[r] = 0
