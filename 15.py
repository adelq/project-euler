from math import factorial

# Combinations
def combin(n, r):
	return factorial(n) / (factorial(r) * factorial(n-r))

# Number of paths in a m x n lattice given by combin(m+n, m)
print(combin(20 + 20, 20))