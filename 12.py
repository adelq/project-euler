from math import sqrt

def FindAllDivisors(x):
	divList = []
	y = 1
	while y <= sqrt(x):
		if x % y == 0:
			divList.append(y)
			divList.append(int(x / y))
		y += 1
	return len(divList)

numgen = 1
while True:
	trianglenumber = numgen*(numgen+1)/2
	if FindAllDivisors(trianglenumber) > 500:
		print trianglenumber
		break
	else:
		numgen += 1