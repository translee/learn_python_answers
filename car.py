"""一个可用于表示汽车的种类"""

class Car():
	"""模拟汽车"""
	
	def __init__(self,make,model,year):
		"""初始化描述汽车的属性"""
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 30   
		
	def get_descriptive_name(self):
		"""返回整洁的描述信息"""
		long_name = str(self.year)+' '+self.make+' '+self.model
		return long_name.title()
	
	def read_odometer(self):
		"""打印一条指出汽车里程的消息"""
		print("This car has "+str(self.odometer_reading)+
		" miles on it.")
		
	def update_odometer(self,mileage):
		"""将里程表读数设置为指定的值,禁止回调"""
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer!")
		
	def increment_odometer(self,miles):
		"""增加指定的量"""
		if miles < 0:
			print('You are too smart!')
		else:
			self.odometer_reading += miles
			

