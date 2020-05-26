"""一组可用于表示电动汽车的类"""

from car import Car

class Battery():
	
	def __init__(self,battery_size=70):
		self.battery_size = battery_size
		
	def describe_battery(self):
		"""描述电瓶容量"""
		print("This car has a "+str(self.battery_size)+"-kwh battery.")
		
	def get_range(self):
		if self.battery_size == 70:
			range = 240
		elif self.battery_size == 85:
			range = 270
		message = "This car can go approximately "+str(range)
		message += " miles on a full charge."
		print(message)
		 
class ElectricCar(Car):
	"""电动车的独特之处"""
	
	def __init__(self,make,model,year):
		"""初始化父类的属性,再初始化特有属性"""
		super().__init__(make,model,year)
		self.battery = Battery()
		
my_tesla = ElectricCar('tesla','model s',2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
