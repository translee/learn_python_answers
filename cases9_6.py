class Restaurant():
	"""餐厅"""
	
	def __init__(self,restaurant_name,cuisine_type):
		"""名称与类型"""
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0
	
	def describe_restaurant(self):
		"""打印上述两条信息"""
		print("\nThe restaurant's name is "+self.restaurant_name.title()+
		'.')
		print("And its cuisine type is "+self.cuisine_type+'.')
	def open_restaurant(self):
		"""营业"""
		print('It is opened now.')
		
	def set_number_served(self,number):
		"""设置就餐人数"""
		self.number_served = number
		
	def increment_number_served(self,increment):
		"""每天人数"""
		self.number_served += increment

class IceCreamStand(Restaurant):
	
	def __init__(self,restaurant_name,cuisine_type):
		super().__init__(restaurant_name,cuisine_type)
		self.flavors = ['apple','milk']
		
	def show(self):
		print(self.flavors)
		


