def main(by):
	diagonal = (by+1)*0.5
	print(spiral(diagonal))

def spiral(d):
	if d == 1:
		return 1
	else:
		downright = 4*d**2-10*d+7
		downleft = 4*d**2-8*d+5
		upleft = 4*d**2-6*d+3
		upright = 4*d**2-4*d+1
		diagonalsum = downright + downleft + upleft + upright
		return diagonalsum + spiral(d-1)


# Test
main(1001)