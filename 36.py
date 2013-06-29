def palindrome(number):
	number = str(number)
	return number == number[::-1]

doublebase = []

for i in range(1000000):
	if palindrome(i):
		if palindrome(str(bin(i)[2::])):
			doublebase.append(i)

print sum(doublebase)