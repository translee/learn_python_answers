def car_info(manufacturer_,model_,**other_info):
	"""car_information"""
	info = {}
	info['manufacturer'] = manufacturer_
	info['model'] = model_
	for key,value in other_info.items():
		info[key] = value
	return info
sb = car_info('subaru','outback',color='blue',tow_package=True)
print(sb)
