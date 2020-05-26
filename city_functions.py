def get_city_and_country(city,country,population=''):
	"""返回城市与国家"""
	if population:
		neatly_form = city.title() + ',' + country.title() +\
		' - population ' + str(population)
	else:
		neatly_form = city.title() + ',' + country.title()
	return neatly_form


