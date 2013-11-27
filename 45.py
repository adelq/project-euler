# Triangular numbers are not needed because they are a subset of hexagonal numbers

def pent(n):
	return n*(3*n-1)/2

def hex(n):
	return n*(2*n-1)

pentset = set(pent(x) for x in range(50000))
hexset = set(hex(x) for x in range(50000))

print pentset & hexset