filename = 'guest_book.txt'
print("You can enter 'q' at any time to quit.")
while True:
	name = input('Please enter your name here: ')
	if name == 'q':
		break
	else:
		with open(filename,'a') as p:
			p.write(name.title()+'\n')
			print('Hello,'+name.title()+'.Welcome to our system.\n')
