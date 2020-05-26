from random import randint

class Die():
	
	def __init__(self,sides=6):
		self.sides = sides
		
	def roll_die(self):
		x = randint(1,self.sides)
		print(x)
		
sb_0 = Die()
for x in range(10):
	sb_0.roll_die()
	
sb_1 = Die(10)
for x in range(10):
	sb_1.roll_die()
	
sb_2 = Die(20)
for x in range(10):
	sb_2.roll_die()
