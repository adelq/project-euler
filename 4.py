def palindrome(number):
	number = str(number)
	return number == number[::-1]

palindromelist = []
for i in range(1000):
	for j in range(i, 1000):
		product = i*j
		if palindrome(product):
			palindromelist.append(product)

print(max(palindromelist))
