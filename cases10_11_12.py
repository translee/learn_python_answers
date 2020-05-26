import json

def get_number():
	"""尝试获取数字"""
	filename = 'favorite_number.json'
	try:
		with open(filename) as f:
			favorite_number = json.load(f)
	except FileNotFoundError:
		return None
	else:
		return favorite_number
		
def input_number():
	favorite_number = input("What's your favorite number? ")
	filename = 'favorite_number.json'
	with open(filename,'w') as f:
		json.dump(str(favorite_number),f)
	return favorite_number
		
def greet_user():
	favorite_number = get_number()
	if favorite_number:
		print("I know your favorite number!It's "+
		str(favorite_number)+'.')
	else:
		favorite_number = input_number()
		print("We will remember your favorite number is "+
		str(favorite_number)+'.')
		
greet_user()
	
	
