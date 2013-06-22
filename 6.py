def sumsq(num):
	s = 0
	for i in range(num + 1):
		s += i**2
	return s

def sqsum(num):
	s = 0
	for i in range(num + 1):
		s += i
	return s**2

def main(num):
	print sqsum(num) - sumsq(num)

main(100)