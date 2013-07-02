from math import factorial

def com(n, r):
	return factorial(n) / (factorial(r)*factorial(n-r))

millionaire = 0
for n in range(1,101):
	for r in range(1,n):
		if com(n,r) > 1000000:
			millionaire += 1
print(millionaire)
