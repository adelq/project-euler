from math import sqrt

def prime(n):
	"""Returns a boolean indicating whether an integer is a prime"""
	if n <= 1:
		return False
	for i in range(2, int(sqrt(n) + 1)):
		if n % i == 0:
			return False
	return True

def upright(d):
	return 4*d**2-10*d+7
def upleft(d):
	return 4*d**2-8*d+5
def downleft(d):
	return 4*d**2-6*d+3
def downright(d):
	return 4*d**2-4*d+1

def percentPrimeSpiral(sideLen):
	diagonalLen = (sideLen+1)/2
	totalDiagonals = (diagonalLen-1)*4 + 1

	numPrimes = 0
	for i in range(1,diagonalLen+1):
		if prime(upright(i)):
			numPrimes += 1
		if prime(upleft(i)):
			numPrimes += 1
		if prime(downright(i)):
			numPrimes += 1	
		if prime(downleft(i)):
			numPrimes += 1
	return numPrimes / float(totalDiagonals)

def main():
	primeRatio = .99
	sideLen = 1001

	while primeRatio > 0.12:
		primeRatio = percentPrimeSpiral(sideLen)
		sideLen += 10
		print primeRatio

	print sideLen
	print primeRatio	

main()