from Node import Node
from Link import Link
from Histogram import Histogram
from Estimator import Estimator

class Predictor:

	def __init__(self, learning_rate):
		self.nodes = []
		self.links = []
		self.pairs = []

		self.inputs  = []
		self.outputs = []
		self.input_links = []

		self.learning_rate = learning_rate

	def create(self, nodes, estimator):
		for i in range(nodes):
			self.nodes.append(Node(estimator))
			self.input_links.append([])

	def connect(self, initial, final, estimator):
		self.links.append(Link(estimator, self.learning_rate))
		self.pairs.append((initial, final))

		index = len(self.links)-1
		self.input_links[final].append(index)

	def set_inputs(self, nodes):
		self.inputs = nodes

	def set_outputs(self, nodes):
		self.outputs = nodes

	def update(self, inputs, time):
		for i in range(len(inputs)):
			n = self.inputs[i]
			self.nodes[n].threshold = 0
			self.nodes[n].state = inputs[i]

		for i in range(len(self.links)):
			ni = self.pairs[i][0]
			nf = self.pairs[i][1]

			si = self.nodes[ni]()
			sf = self.nodes[nf]()

			self.links[i].update((si, sf), time)

		for i in range(len(self.nodes)):
			x = []

			for l in self.input_links[i]:
				x.append(self.links[l]())

			self.nodes[i].update(x)

		outputs = []
		
		for y in self.outputs:
			outputs.append(self.nodes[y]())

		return outputs

	def error(self):
		error = 0
		for i in range(len(self.links)):
			error += self.links[i].error
		return error/len(self.links)

