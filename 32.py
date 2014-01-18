pan = set("123456789")

def isPandigital(n):
	"""Returns a boolean indicating whether a number is pandigital"""
	n = set(str(n))
	if n == pan:
		return True
	else:
		return False

def main():
	productsList = []

	# Covers 2 digits * 3 digits
	for i in range(10,99):
		for j in range(100,999):
			product = i*j
			if len(str(product)) == 4:
				if isPandigital(str(i) + str(j) + str(product)):
					if product not in productsList:
						productsList.append(product)
						print(i,j,product)
	
	# Covers 1 digit * 4 digits
	for i in range(2,9):
		for j in range(1000,9999):
			product = i*j
			if len(str(product)) == 4:
				if isPandigital(str(i) + str(j) + str(product)):
					if product not in productsList:
						productsList.append(product)
						print(i,j,product)

	return sum(productsList)

print(main())