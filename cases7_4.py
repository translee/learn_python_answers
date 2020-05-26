prompt="Please enter the toppings here: "
prompt+="\nEnter 'quit' to finish it. "
while True:
	message=input(prompt)
	if message=='quit':
		break
	print("OK,we will add "+message+" to your pizza.")
