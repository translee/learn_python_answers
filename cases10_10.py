filename = 'little_women.txt'

with open(filename) as f:
	contents = f.read()
	number = contents.lower().count('the')
	print(number)
