# Same code used for problem 18

def loadTriangle():
	"""
	Returns a list of lists for the triangle stored in file
	"""
	f = open("67_triangle.txt", 'r')
	triangle = f.read().split("\n")
	for row in range(len(triangle)):
		triangle[row] = map(int, triangle[row].split())
	return triangle

def addBottom(triangle):
	"""
	Adds maximum values from the bottom row to the row above, reducing the
	number of rows in the triangle
	"""
	newTriangle = triangle[:-1]
	
	# maxBottom is a list that contains the maximum values corresponding to the
	# second to last row
	maxBottom = []
	for s in range(0,len(triangle[-1])-1):
		b = s + 1
		maxBottom.append(max([triangle[-1][s],triangle[-1][b]]))
	
	# Adds value of maxBottom to second to last row in the new triangle
	for value in range(len(newTriangle[-1])):
		newTriangle[-1][value] += maxBottom[value]

	return newTriangle

def main():
	""" Main loop, iterates through triangle until only top value is left """
	triangle = loadTriangle()
	while len(triangle) > 1:
		triangle = addBottom(triangle)
	return triangle[0][0]

print main()