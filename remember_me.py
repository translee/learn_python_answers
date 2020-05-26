import json

def get_stored_username():
	"""如果存储了用户名，就获取它"""
	filename = 'username.json'
	try:
		with open(filename) as f_obj:
			username = json.load(f_obj)
	except FileNotFoundError:
		return None
	else:
		return username
		
def get_new_user_name():
	"""提示用户输入用户名"""
	username = input("What's your name? ")
	filename = 'username.json'
	with open(filename,'w') as f_obj:
		json.dump(username.title(),f_obj)
	return username
			
def greet_user():
	"""问候用户，并指出其名字"""
	username = get_stored_username()
	if username:
		correct = input("Are you "+username+'?(y/n) ')
		if correct == 'y':
			print("Welcom back, "+username+"!")
		else:
			username = get_new_user_name()
			print("We will remember you when you come back, "+
		username.title()+'!')
		
	else:
		username = get_new_user_name()
		print("We will remember you when you come back, "+
		username.title()+'!')

greet_user()
