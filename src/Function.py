e = 2.718281828459

def sigmoid(x, a, b, c):
	return a / (1+pow(e, -c * (x-b)))

def gaussian(x, a, b, c):
	return a * pow(e, -pow(x-b, 2) / pow(2*c, 2))