fibonaccinumbers = {0: 0, 1: 1}

def fib(n):
	if n not in fibonaccinumbers:
		fibonaccinumbers[n] = fib(n-1) + fib(n-2)
	return fibonaccinumbers[n]

x = 0
while len(str(fib(x))) < 1000:
	x += 1
print(x)