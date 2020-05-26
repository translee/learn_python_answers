print("Give me two numbers,and I'll divide them.")
print("Enter 'q' to quit.")

while True:
	first_number = input("\nFirst number: ")
	if first_number == 'q':
		break
	try:
		x = int(first_number)
	except ValueError:
		print("You can't enter words!")
		continue
	second_number = input("Second number: ")
	if second_number == 'q':
		break
	try:
		y = int(second_number)
	except ValueError:
		print("You can't enter words!")
		continue
	sum = x + y
	print("The sum of "+str(first_number)+" and "+str(second_number)+
	" is "+str(sum)+'.')
