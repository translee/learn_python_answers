filename = 'learning_python.txt'
with open(filename) as file_object:
	lines = file_object.readlines()
for line in lines:
	sb = line.replace('python','C')
	print(sb.rstrip())
