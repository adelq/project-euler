champ = ""

concat = 1
while len(champ) < 1000010:
	champ += str(concat)
	concat += 1

print(int(champ[0]) * int(champ[9]) * int(champ[99]) * int(champ[999]) * int(champ[9999]) * int(champ[99999]) * int(champ[999999]))