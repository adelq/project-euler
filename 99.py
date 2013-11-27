from math import log10

# Input file IO
f = open("base_exp.txt", "r")
f = f.read().split()

# Initial variables
maxLine = list(map(float,f[0].split(",")))
maxLineNumber = ""

# Loops through to find biggest numbers
# Uses log10 to avoid exponentiation complexity
for line in f:
	exp = line.split(",")
	exp = list(map(float, exp))
	if (exp[1]*log10(exp[0])) > (maxLine[1]*log10(maxLine[0])):
		maxLine = exp
		maxLineNumber = f.index(line)

print(maxLine)
print(maxLineNumber + 1)