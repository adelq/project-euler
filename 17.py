# Dictionaries that map from number to number of letters
ones = {
	0: 0,                   # 'one'
	1: 3,                   # 'two'
	2: 3,
	3: 5,
	4: 4,
	5: 4,
	6: 3,
	7: 5,
	8: 5,
	9: 4,
	}
teens = {
	10: 3,                  # 'ten'
	11: 6,                  # 'eleven'
	12: 6,
	13: 8,
	14: 8,
	15: 7,
	16: 7,
	17: 9,
	18: 8,
	19: 8,
	}
tens = {
	2: 6,                   # 'twenty'
	3: 6,                   # 'thirty'
	4: 5,
	5: 5,
	6: 5,
	7: 7,
	8: 6,
	9: 6,
	}
hundred = {
	0: 10,                  
	1: 13,                  # 'one hundred and '
	2: 13,                  # 'two hundred and '
	3: 15,
	4: 14,
	5: 14,
	6: 13,
	7: 15,
	8: 15,
	9: 14,
	}

def number_length(n):
	if n < 10:
		return ones[n]
	elif n < 100:
		if n < 20:
			return teens[n]
		else:
			return tens[n/10] + ones[n % 10]
	elif n < 1000:
		if n % 100 == 0:
			return ones[n/100] + 7 # Add 7 for length of 'hundred'
		else:
			return hundred[n/100] + number_length(n % 100)

def main(n):
	total = 0
	for i in xrange(1, n):
		total += number_length(i)
	return total + 11 # Add 11 for length of 'one thousand'

if __name__ == "__main__":
	print main(1000)
