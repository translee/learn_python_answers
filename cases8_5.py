def describe_city(name,country='china'):
	"""城市名字及国家"""
	print(name.title()+' is in '+country.title()+'.')
describe_city('shanghai')
describe_city('beijing')
describe_city('moscow','russia')
