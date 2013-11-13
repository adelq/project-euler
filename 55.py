def isPalindrome(n):
	"""Returns a boolean indicating whether a number is a palindrome"""
	n = str(n)
	return n == n[::-1]

def reverseAdd(n):
	"""Take number and add reverse"""
	return n + int(str(n)[::-1])

def isLychrel(n):
	"""Returns a boolean indicating if the number is a Lychrel number"""
	iterations = 0
	n = reverseAdd(n)

	# Maximum of 50 iterations
	while iterations < 50:
		if isPalindrome(n):
			return False
		else:
			iterations += 1
			n = reverseAdd(n)
	return True

def main(limit):
	"""Iterates through all numbers up to limit to find Lychrel numbers"""
	numberLychrels = 0

	for i in range(1, limit):
		if isLychrel(i):
			numberLychrels += 1
	return numberLychrels

print(main(10000))