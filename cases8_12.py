def make_sandwich(*toppings):
	"""三明治"""
	print('\nMaking a sandwich with the following toppings:')
	for topping in toppings:
		print('- '+topping)
make_sandwich('pepper')
make_sandwich('pepper','mushrooms')
make_sandwich('pepper','mushrooms','meat')
