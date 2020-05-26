def make_album(singer,song):
	"""ddd"""
	llll = {'singer_':singer,'song_':song}
	return llll
while True:
	print("Enter 'q' at any time to quit")
	singer = input('singer: ')
	if singer == 'q':
		break
	song=input('song: ')
	if song == 'q':
		break
	sb = make_album(singer,song)
	print(sb)
