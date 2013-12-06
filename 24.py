from itertools import permutations

lexorder = 1

for permutation in permutations("0123456789", 10):
	if lexorder == 1000000:
		print(''.join(permutation))
	lexorder += 1