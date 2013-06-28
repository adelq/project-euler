from math import factorial

num = str(factorial(100))

sum = 0
for i in num:
	sum += int(i)

print sum