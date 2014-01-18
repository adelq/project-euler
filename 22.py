import string
letterscore = dict(list(zip(string.ascii_lowercase, list(range(1, 27)))))

f = open("names.txt", "r")
f = f.read()
f = f.strip().split(',')
f.sort()

for index in range(len(f)):
	f[index] = f[index][1:-1]

namelist = [x.lower() for x in f]

namescoresum = 0
for i in range(len(namelist)):
	wordscore = 0
	for char in namelist[i]:
		wordscore += letterscore[char]
	namescoresum += (i + 1) * wordscore

print(namescoresum)