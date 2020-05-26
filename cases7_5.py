prompt="Please enter your age here so that we can tell you the ticket\
 prices: "
prompt+="\nEnter 'quit' to finish. "
while True:
	age=input(prompt)
	if age=='quit':
		print("good bye")
		break
	elif int(age)<3:
		print("The price is free.")
	elif int(age)<=12:
		print("The price is 10 dollar.")
	elif int(age)>12:
		print("The price is 15 dollar.")
