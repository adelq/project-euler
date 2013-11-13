# Set to check if a number is pandigital
pan = set("123456789")

# Not used in this problem but may come in handy
# def setmaker(n):
# 	return set(x for x in str(n))

def concatProduct(n, pan):
	"""
	Input is a fixed number and a list, function will return concatenated
	product of the fixed number with individual elements of the list
	"""
	product = ""
	for i in pan:
		product += str(n*i)
	return product

def isPandigital(n):
	"""Returns a boolean indicating whether a number is pandigital"""
	nset = set(str(n))
	if nset == pan and len(n) == 9:
		return True
	else:
		return False

maxProduct = 918273645

# Main loop, solution set contained to 4 digit numbers that are greater than the
# result given in the prompt by 9 and (1,2,3,4,5)
for fixed in range(9000,10000):
	concatenatedProduct = concatProduct(fixed, (1,2))
	if isPandigital(concatenatedProduct):
		if concatenatedProduct > maxProduct:
			maxProduct = concatenatedProduct

print(maxProduct)