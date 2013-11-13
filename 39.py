def pythsolutions(p):
	"""Return the number of valid Pythagorean triples with given perimeter (must be int)"""
	rightlist = []
	for x in range(1,p):
		y = x + 1
		z = y + 1
		while z <= p:
			while z**2 < x**2 + y**2:
				z += 1
			if z**2 == x**2 + y**2 and z <= p and x + y + z == p:
				rightlist.append([x, y, z])
			y += 1
	return len(rightlist)

# Max number of solutions
maxsolutions = 1
# Perimeter for the max number of solutions
bestpsolution = 1
for i in range(1000):
	numsolutions = pythsolutions(i)
	if numsolutions > maxsolutions:
		bestpsolution = i
		maxsolutions = numsolutions

print(bestpsolution)