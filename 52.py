def numhash(num):
	num = str(num)
	digithash = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
	for digit in num:
		digithash[int(digit)] += 1
	return digithash

i = 1
while True:
	spechash = numhash(i)
	if spechash == numhash(2*i):
		if spechash == numhash(3*i):
			if spechash == numhash(4*i):
				if spechash == numhash(5*i):
					if spechash == numhash(6*i):
						print(i)
						break
					else:
						i+=1
				else:
					i+=1
			else:
				i+=1
		else:
			i+=1
	else:
		i += 1
