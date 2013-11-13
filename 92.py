def sqdigits(num):
	num = str(num)
	sum = 0
	for char in num:
		sum += int(char)**2
	return sum

def digchain(num):
	if num == 1:
		return 1
	elif num == 89:
		return 89
	else:
		return digchain(sqdigits(num))
num89 = 0

for i in range(1,10000000):
	if digchain(i) == 89:
		num89 += 1

print(num89)
