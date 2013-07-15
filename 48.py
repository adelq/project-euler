series = 0
for i in range(1,1000):
	series += pow(i,i)

print(str(series)[-10::])
