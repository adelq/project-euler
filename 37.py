from math import sqrt

def prime(n):
	"""Checks whether a number is prime"""
	n = int(n)
	if n == 1:
		return False
	for i in range(2, int(sqrt(n) + 1)):
		if n % i == 0:
			return False
	return True

def digremoval(n):
	"""Returns a list with all the truncated versions of the inputted integer from both left and right"""
	n = str(n)
	nlist = [n]
	for i in range(1, len(n)):
		nlist.append(n[i::])
		nlist.append(n[:i:])
	return nlist

def truncatable(n):
	"""Returns whether all truncated versions of the integer are prime"""
	n = str(n)
	# nlist is the list of all truncates
	nlist = digremoval(n)
	for i in nlist:
		if not prime(i):
			return False
	return True

truncprimes = []
numgen = 8
# Loops until there are 11 truncatable primes
while len(truncprimes) < 11:
	if truncatable(numgen):
		truncprimes.append(numgen)
	numgen += 1

print(sum(truncprimes))