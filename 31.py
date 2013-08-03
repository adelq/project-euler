# Global variables. Total is £2, so 200 pence.
total = 200
ways = 0

# a is 200p
# b is 100p
# c is 50p
# d is 20p
# e is 10p
# f is 5p
# g is 2p
# h is 1p

# Loop goes through each coin from the total to the amount left stored in the
# previous variable to 0, and decreases the amount left with the value of the
# coin. Each loop increases the number of ways by one.

for a in range(total, -1, -200):
	for b in range(a, -1, -100):
		for c in range(b, -1, -50):
			for d in range(c, -1, -20):
				for e in range(d, -1, -10):
					for f in range(e, -1, -5):
						for g in range(f, -1, -2):
							ways += 1

print ways