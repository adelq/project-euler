def fib(n):
	if n == 0:
		return 0
	if n == 1:
		return 1
	else:
		return fib(n-1) + fib(n-2)

fiblist = []
for i in range(1,34):
	fiblist.append(fib(i))

summation = 0
for i in range(33):
	if fiblist[i] % 2 == 0:
		summation += fiblist[i]

print(summation)