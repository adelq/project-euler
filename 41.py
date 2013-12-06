from itertools import permutations
from math import sqrt

digits = "1234567"
maxPrime = 0


def prime(n):
	"""Returns a boolean indicating whether an integer is a prime"""
	if n <= 1:
		return False
	for i in range(2, int(sqrt(n) + 1)):
		if n % i == 0:
			return False
	return True

for i in permutations(digits, len(digits)):
	# Reduce tuples into a string
	i = int(''.join(i))
	
	if prime(i):
		if i > maxPrime:
			maxPrime = i

print(maxPrime)