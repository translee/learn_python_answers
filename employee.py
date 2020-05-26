class Employee():
	
	def __init__(self,first,last,salary):
		self.first_name = first
		self.last_name = last
		self.salary = salary
		
	def give_raise(self,amount=5000):
		self.salary += amount
		
