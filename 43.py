from string import digits
from itertools import permutations

substringDivisibility = 0

for i in permutations(digits, 10):
	# Reduce tuples into a string
	i = ''.join(i)
	
	# Create list of all list triplets
	divisibilityList = list(map(int, [i[1:4], i[2:5], i[3:6], i[4:7], i[5:8], i[6:9], i[7:10]]))

	# Check for all divisibility rules
	if divisibilityList[0] % 2 == 0 and divisibilityList[1] % 3 == 0 and divisibilityList[2] % 5 == 0 and divisibilityList[3] % 7 == 0 and divisibilityList[4] % 11 == 0 and divisibilityList[5] % 13 == 0 and divisibilityList[6] % 17 == 0:
		substringDivisibility += int(i)
		print(i)

print(substringDivisibility)