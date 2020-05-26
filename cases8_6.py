def city_country(city,country):
	"""城市与国家"""
	message='"'+city.title()+','+country.title()+'"'
	return message
sb=city_country('beijing','china')
print(sb)
