magicians = ['liuqian','sb','sss']
the_great_magicians = []
def make_great(magicians,the_great_magicians):
	"""了不起"""
	while magicians:
		magician = magicians.pop()
		the_great_magician = 'the Great '+magician.title()
		the_great_magicians.append(the_great_magician)
def show_magicians(the_great_magicians):
	"""打印名字"""
	for name in the_great_magicians:
		print(name)
make_great(magicians[:],the_great_magicians)
show_magicians(the_great_magicians)
show_magicians(magicians)
