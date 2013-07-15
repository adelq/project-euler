from math import sqrt

def d(x):
	"""Returns sum of divisors of given integer"""
	divList = []
	y = 1
	while y <= sqrt(x):
		if x % y == 0:
			divList.append(y)
			divList.append(int(x / y))
		y += 1
	divList.remove(x)
	return sum(divList)

amicablesum = 0
for a in range(1,10000):
	b = d(a)
	if d(a) == b and d(b) == a and b != 1 and a != b:
		amicablesum += a

print amicablesum