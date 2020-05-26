def build_profile(first,last,**user_info):
	"""创建一个字典"""
	profile={}
	profile['first_name'] = first
	profile['last_name'] = last
	for key,value in user_info.items():
		profile[key] = value
	return profile
user_profile = build_profile('li','hui',location='changan',age='21')
print(user_profile)
