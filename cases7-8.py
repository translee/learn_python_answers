#公告
print('Notice:Sorry,the pastrami has sold out.')
sandwich_orders=['tuna','ddddf','ssdff','dffggg','pastrami','pastrami']
finished_sandwiches=[]
#剔除
while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')
while sandwich_orders:
	sb=sandwich_orders.pop()
	print("I made your "+sb+' sandwich.')
	finished_sandwiches.append(sb)
print('\nThese are your sandwiches:')
#核实
for finished_sandwiche in finished_sandwiches:
	print(finished_sandwiche)
