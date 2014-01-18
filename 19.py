from datetime import date

sundays = 0

for year in range(1901,2001):   # From 1901 to 2000
	for month in range(1,13): # Every month
		# Check if first day of the month is Sunday (6)
		if date(year, month, 1).weekday() == 6:
			sundays += 1

print(sundays)
