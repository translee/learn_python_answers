def greet_users(names):
	"""问候每个用户"""
	for name in names:
		msg = "Hello, "+name.title()+'!'
		print(msg)
usernames = ['laoniu','lihui','sb','hhhh']
greet_users(usernames)
