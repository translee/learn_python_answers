def make_shirt(size,letters='I love Python'):
	"""尺码，有默认字样"""
	print('This shirt is '+size.title()+' size and printed "'+letters+\
'".')
make_shirt('L')
make_shirt(size='L')
make_shirt('M')
make_shirt('S','fuck you')
make_shirt(size='S',letters='fuck you')
make_shirt(letters='fuck you',size='S')
make_shirt('S',letters='fuck you')



