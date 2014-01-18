import unittest

def isIncreasing(n):
	"""
	Returns boolean whether number is increasing
	Decreasing defined as whether next digit is larger or equal
	"""
	s = str(n)
	b = True
	for i in range(len(s) - 1):
		if int(s[i]) > int(s[i + 1]):
			b = False
	return b

def isDecreasing(n):
	"""
	Returns boolean whether number is decreasing
	Decreasing defined as whether next digit is smaller or equal
	"""
	s = str(n)
	b = True
	for i in range(len(s) - 1):
		if int(s[i]) < int(s[i + 1]):
			b = False
	return b

def isBouncy(n):
	"""
	Returns boolean whether number is bouncy
	Bouncy defined as not increasing or decreasing
	"""
	return not (isIncreasing(n) or isDecreasing(n))

def main(n):
	bouncy = 0.0            # Number of bouncy numbers so far
	total = 0               # Also functions as a counter
	prop = 0.0              # Proportion of bouncy numbers

	while prop < n:
		total += 1
		if isBouncy(total):
			bouncy += 1
		prop = bouncy / total

	return total

# Testing suite
# Based on Project Euler description
class Bouncy(unittest.TestCase):
	def test_increasing(self):
		self.assertTrue(isIncreasing(134468))
		self.assertFalse(isIncreasing(66420))
		self.assertFalse(isIncreasing(155349))
	def test_decreasing(self):
		self.assertFalse(isDecreasing(134468))
		self.assertTrue(isDecreasing(66420))
		self.assertFalse(isDecreasing(155349))
	def test_bouncy(self):
		self.assertFalse(isBouncy(134468))
		self.assertFalse(isBouncy(66420))
		self.assertTrue(isBouncy(155349))

	def test_50bouncy(self):
		self.assertEqual(538, main(0.5))

	def test_90bouncy(self):
		self.assertEqual(21780, main(0.9))

if __name__ == "__main__":
	print main(0.99)
	unittest.main()
