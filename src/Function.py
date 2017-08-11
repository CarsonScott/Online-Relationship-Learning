e = 2.718281828459

def sigmoid(x, a, b, c):
	return a / (1+pow(e, -c * (x-b)))