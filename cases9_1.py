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
restaurant = Restaurant('zilanyuan','school dynasty')
restaurant.set_number_served(20)
restaurant.increment_number_served(10)
print("There has been "+str(restaurant.number_served)+
" people eaten here.")
