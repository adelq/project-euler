def numsum(num):
	num = str(num)
	numsum = 0
	for digit in num:
		numsum += int(digit)
	return numsum

maxsum = 0
for a in range(1,100):
	for b in range(1,100):
		digitsum = numsum(pow(a,b))
		if digitsum > maxsum:
			maxsum = digitsum

print(maxsum)
