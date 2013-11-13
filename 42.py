import string
letterscore = dict(list(zip(string.ascii_lowercase, list(range(1, 27)))))
triangle = [x*(x+1)/2 for x in range(1000)]

f = open("words.txt", "r")
f = f.read()
f = f.strip().split(',')
f.sort()

for index in range(len(f)):
	f[index] = f[index][1:-1]

wordlist = [x.lower() for x in f]

trianglewords = 0
for word in wordlist:
	wordscore = 0
	for char in word:
		wordscore += letterscore[char]
	if wordscore in triangle:
		trianglewords += 1

print(trianglewords)