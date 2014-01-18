from math import sqrt

def prime(n):
	for i in range(2, int(sqrt(n) + 1)):
		if n % i == 0:
			return False
	return True

primes = []
i = 1

while len(primes) < 10001:
	i += 1
	if prime(i):
		primes.append(i)

print(i)