N = 800
pythlist = []

for x in range(N):
	y = x+1
	z = y+1
	while z <= N:
		while z * z < x * x + y * y:
			z = z + 1
		if z * z == x * x + y * y and z <= N:
			if x != 0 and y != 0 and z != 0:
				pythlist.append([x, y, z])
		y = y + 1

for triplet in pythlist:
	tripsum = triplet[0] + triplet[1] + triplet[2]
	if tripsum == 1000:
		print(triplet[0] * triplet[1] * triplet[2])