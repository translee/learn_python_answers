filenames = ['dogs.txt','cats.txt']

for filename in filenames:
	try:
		with open(filename) as p:
			sb = p.read()
	except FileNotFoundError:
		pass
	else:
		print("\nReading file: "+filename)
		print(sb)
