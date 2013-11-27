from itertools import product,cycle,izip

def loadWords():
	"""
	Returns a list of valid words. Words are strings of lowercase letters.
	
	Depending on the size of the word list, this function may
	take a while to finish.
	"""
	print "Loading word list from file..."
	inFile = open("59_words.txt", 'r')
	wordList = inFile.read().split()
	print "  ", len(wordList), "words loaded."
	return wordList

wordList = loadWords()

def getCipherList():
	"""
	Returns cipher in encrypted list.
	"""
	return open("cipher1.txt", "r").read().strip('\n').split(",")

def isWord(wordList, word):
	"""
	Determines if word is a valid word.

	wordList: list of words in the dictionary.
	word: a possible word.
	returns True if word is in wordList.

	Example:
	>>> isWord(wordList, 'bat') returns
	True
	>>> isWord(wordList, 'asdf') returns
	False
	"""
	word = word.lower()
	word = word.strip(" !@#$%^&*()-_+={}[]|\\:;'<>?,./\"")
	return word in wordList

def numWords(decryptedText):
	""" Returns the number of valid words there are in given text """
	decryptedList = decryptedText.split()
	wordCount = 0

	for word in decryptedList:
		if isWord(wordList, word):
			wordCount += 1

	return wordCount

def ascii(cipherList):
	""" Takes list of ASCII codes as input, returns concatenated string """
	decryptedList = []
	for char in cipherList:
		decryptedList.append(chr(int(char)))
	
	return "".join(map(chr, map(int, cipherList)))

def decrypt(key):
	""" Decrypts story using given key using an XOR cipher """
	data = ascii(getCipherList())
	return "".join(chr(ord(x) ^ ord(y)) for (x,y) in izip(data, cycle(key)))

def asciisum(text):
	""" Returns the sum of ASCII codes in a given string """
	text = list(text)
	text = map(ord, text)
	return sum(text)

def main():
	"""
	Main wrapper function.

	Generates all possible keys, then iterates through them to find the one that
	decrypts the original ciphertext into the maximum number of English words.
	The function returns the sum of the ASCII codes of the resulting decrypted
	text.
	"""
	lowercase = map(chr, range(97, 123))

	# Generate a list of possible keys
	keylist = []
	for key in product(lowercase, repeat=3):
		keylist.append("".join(key))
	
	currentNumWords = 0
	maxWords = 0
	bestKey = ""

	for key in keylist:
		currentNumWords = numWords(decrypt(key))
		if currentNumWords > maxWords:
			maxWords = currentNumWords
			bestKey = key

	return asciisum(decrypt(bestKey))

print main()