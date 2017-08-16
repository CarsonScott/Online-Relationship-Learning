from Predictor import *
from Histogram import Histogram
from random import randrange as rr
from math import floor

h = Histogram(100, 100)
e = Estimator(h)

e.setgrowth(10,10)
e.setdecay(10,10)
e.g_rate = 0.0006
e.d_rate = 0.0006

nodes = 30
links = round(nodes*1.2)

p = Predictor(0.0003)
p.create(nodes, e)

for i in range(links):
	ni = rr(nodes)
	nf = rr(nodes)

	if i < nodes:
		ni = i
	p.connect(ni, nf, e)

p.set_inputs([i for i in range(10)])
p.set_outputs([i for i in range(nodes)])

inputs = []
for i in range(30):
	x = []
	for j in range(len(p.inputs)):
		x.append(round(rr(100)/100))
	inputs.append(x)

f = open('log.txt', 'w')

j = 0
for i in range(6000):
	x = inputs[j]
	y = p.update(x, i)

	string = ''
	for k in y:
		if k != 0: string += '+'
		else: string += ' '
	print(string, j)

	j += 1
	if j >= len(inputs):
		j = 0
		print('---------------------------------------------------------------')

	f.write(str(p.total_error()) + '\n')