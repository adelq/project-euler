# Global variable for number of n-digit positive integers exist which are also an nth power
powerful = 0

for power in range(1,100):
	# Create upper and lower bounds for the number of digits
	lowerbound = 10**(power-1)
	upperbound = 10**power
	
	# Counter variables
	counter = 1
	currentpower = 1

	while currentpower < upperbound:
		currentpower = counter**power
		
		# Optional status indicators for testing - not intended for production
		# print "Current value of expression: " + str(currentpower)
		# print "Bounds are from " + str(lowerbound) + " < x < " + str(upperbound)
		
		if currentpower >= lowerbound and currentpower < upperbound:
			print(counter**power)
			powerful += 1
		counter += 1
print(powerful)	