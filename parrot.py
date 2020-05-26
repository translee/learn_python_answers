prompt="Tell me something,and I will reapeat it back to you: "
prompt+="\nEnter 'quit' to end the program. "
active=True
while active:
	message=input(prompt)
	if message=='quit':
		active=False
	else:
		print(message)
