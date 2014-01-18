from fractions import Fraction

tens = []
for n in range(1,10):
	for d in range(n+1,10):
		tens.append(Fraction(n,d))

fractionsum = 1

for num in range(10,100):
	for den in range(num+1,100):
		# This case does not result in any solutions
		# if str(num)[0] == str(den)[1]:
		# 	if Fraction(num,den) == Fraction(int(str(num)[1]) , int(str(den)[0])):
		# 		print num
		# 		print den
		if str(den)[0] == str(num)[1]:
			if float(str(den)[1]) != 0:
				if Fraction(num,den) == Fraction(int(str(num)[0]) , int(str(den)[1])):
					fractionsum *= Fraction(num,den)

print(fractionsum)
