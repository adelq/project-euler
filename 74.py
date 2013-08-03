from math import factorial

def digitFactorial(n):
	"""Takes integer and returns the sum of the factorial of its digits"""
	n = str(n)
	
	factorialSum = 0
	
	for digit in n:
		digit = int(digit)
		factorialSum += factorial(digit)

	return factorialSum

def isDigitFactorial(n):
	"""Checks if number is one of the 4 loops given in prompt, method not used in solution"""
	if n == 145 or n == 169 or n == 871 or n == 872:
		return True
	else:
		return n == digitFactorial(n)

def isChainDigitFactorial(n):
	"""Returns a boolean indicating if the number is a non-repeating digit factorial"""
	iterations = 1
	terms = [n]

	# Maximum of 50 iterations
	while iterations < 60:
		n = digitFactorial(n)

		if n in terms:
			return False
		else:
			terms.append(n)
			iterations += 1
	return True

def main(limit):
	"""Iterates through all integers up to limit to find non-repeating terms"""
	numberFactorialChains = 0

	for i in range(1, limit):
		if isChainDigitFactorial(i):
			numberFactorialChains += 1
	return numberFactorialChains

print main(1000000)