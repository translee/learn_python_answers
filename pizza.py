def make_pizza(*toppings):
	"""打印配料"""
	print("\nMaking a pizza with the following toppings:")
	for topping in toppings:
		print("- "+topping)
make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')

