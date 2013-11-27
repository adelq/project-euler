from math import sqrt

def prime(n):
	"""Returns a boolean indicating whether an integer is a prime"""
	if n <= 1:
		return False
	for i in range(2, int(sqrt(n) + 1)):
		if n % i == 0:
			return False
	return True

# Set of helper functions along each diagonal
def upright(d):
	return 4*d**2-10*d+7
def upleft(d):
	return 4*d**2-8*d+5
def downleft(d):
	return 4*d**2-6*d+3
def downright(d):
	return 4*d**2-4*d+1

# Starting values for while loop
primeRatio = 1.0
sideLen = 3
numPrimes = 0

while primeRatio > 0.10:
	diagonalLen = (sideLen+1)/2
	totalDiagonals = (diagonalLen-1)*4 + 1

	if prime(upright(diagonalLen)):
		numPrimes += 1
	if prime(upleft(diagonalLen)):
		numPrimes += 1
	if prime(downright(diagonalLen)):
		numPrimes += 1	
	if prime(downleft(diagonalLen)):
		numPrimes += 1

	primeRatio = numPrimes / float(totalDiagonals)
	sideLen += 2

# Adjust sidelength by 2
print sideLen - 2
print primeRatio