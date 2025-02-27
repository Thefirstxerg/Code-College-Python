def build_profile(first, last, **user_info): # ** creates an empty dictionary called user_info, like the singular * creates an empty tuple
                                             # ,the double ** creates an empty dictionary
	"""Build a dictionary containing everything we know about a user."""
	user_info['first_name'] = first
	user_info['last_name'] = last
	return user_info

user_profile = build_profile('albert', 'einstein',
	location='princeton',
	field='physics')
print(user_profile)