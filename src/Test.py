from Node import *
from Relation import *

h = Histogram(100, 100)
e = Estimator(h)
e.setgrowth(5, 5)
e.setdecay(0, 5)
e.g_rate = 0.009
e.g_rate = 0.0009

r = Relation(e)

for i in range(100):
	if i % 10 == 0:
		y = r.update((1, 0), i)
	elif i % 5 == 0:
		y = r.update((0, 1), i)
	else:
		y = r.update((0, 0), i)

	print(y)