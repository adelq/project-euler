from math import factorial

factorialdigit = []
for num in range(3,100000):
	strsum = 0
	for i in str(num):
		strsum += factorial(int(i))
	if num == strsum:
		factorialdigit.append(num)

print sum(factorialdigit)