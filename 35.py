from math import sqrt

def prime(n):
	"""Returns a boolean indicating whether an integer is a prime"""
	if n <= 1:
		return False
	for i in range(2, int(sqrt(n) + 1)):
		if n % i == 0:
			return False
	return True

def rotate(n):
	"""Returns a list of all rotations of a number"""
	n = str(n)
	rotationslist = []
	
	rot = n
	while rot not in rotationslist:
		rotationslist.append(rot)
		rot = rot[-1] + rot[:-1]

	return list(map(int,rotationslist))

def isCircularPrime(n):
	"""Returns boolean whether all rotations of digits are prime"""
	rotations = rotate(n)

	for permutation in rotations:
		if prime(permutation) == False:
			return False
	return True

def main(n):
	"""Main thread for the program"""
	numberCircularPrimes = 0
	
	for i in range(n):
		if prime(i):
			if isCircularPrime(i):
				numberCircularPrimes += 1

	return numberCircularPrimes

print(main(1000000))