from math import sqrt

def prime(n):
	for i in range(2, int(sqrt(n) + 1)):
		if n % i == 0:
			return False
	return True

primes = [2]
i = 2

while primes[-1] < 2000000:
	i += 1
	if prime(i):
		primes.append(i)

primes.pop()
print(sum(primes))