def collatz(num):
	if num % 2 == 0:
		return num / 2.0
	else:
		return 3*num + 1

def seq(num):
	chain = 1
	while num != 1:
		num = collatz(num)
		chain += 1
	return chain

def main():
	maxnum = 0
	max = 0
	for i in range(1,1000000):
		if seq(i) > max:
			maxnum = i
			max = seq(i)
	return maxnum

print(main())