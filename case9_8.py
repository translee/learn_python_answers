"""用户大类"""

class User():
	"""用户信息"""
	
	def __init__(self,first_name,last_name):
		"""名字"""
		self.first_name = first_name
		self.last_name = last_name
		self.login_attempts = 0
		
	def describe_user(self):
		"""信息摘要"""
		print("First name is "+self.first_name.title()+'.')
		print("Last name is "+self.last_name.title()+'.')
		
	def greet_user(self):
		"""打招呼"""
		full_name = self.first_name.title()+' '+self.last_name.title()
		print("Hello, "+full_name+'!')
		
	def increment_login_attepmts(self):
		"""plus_1"""
		self.login_attempts += 1
		
	def reset_login_attempts(self):
		"""重置为0"""
		self.login_attempts = 0
		


