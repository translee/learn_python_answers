name = input('Enter your name here: ')
filename = 'guest.txt'
with open(filename,'w') as p:
	p.write(name.title()) 
