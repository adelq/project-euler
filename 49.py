from math import sqrt
from math import fabs

def prime(n):
	"""Returns a boolean indicating whether an integer is a prime"""
	if n <= 1:
		return False
	for i in range(2, int(sqrt(n) + 1)):
		if n % i == 0:
			return False
	return True

def isPermutation(a, b):
	"""Returns a boolean indicating whether the two numbers are permutations of each other"""
	a = str(a)
	b = str(b)
	return sorted(a) == sorted(b)

primesList = []

# Create a list of all primes between the two values
for i in range(1000, 10000):
	if prime(i):
		primesList.append(i)

midpointList = []

# Create a list of all equidistant triples of primes
for i in primesList:
	for j in primesList:
		if int((i + j)/2) in primesList:
			midpointList.append([i, int((i + j)/2), j, fabs((i - j)/2)])

permutationList = []

# Create a list of all triples that are permutations of each other
for sequence in midpointList:
	if isPermutation(sequence[0], sequence[1]) and sequence[0] != sequence[1]:
		if isPermutation(sequence[1], sequence[2]) and sequence[1] != sequence[2]:
			permutationList.append(sequence)

# Print out resulting 12-digit number
for i in permutationList:
	for j in range(len(i)):
		i[j] = str(i[j])
	print("".join(i[:-1]))