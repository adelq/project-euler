fifthlist = []
for number in range(1000000):
	fifthsum = 0
	for digit in str(number):
		fifthsum += int(digit)**5
	if fifthsum == number and number > 1 and number not in fifthlist:
		fifthlist.append(number)
print fifthlist