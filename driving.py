country = input('What country are you from:') 
if country == 'America' or country == 'Taiwan':
	age = int(input('how old are you:'))
	if country == 'Taiwan':
		if age >= 18:
			print("you can have drivers' license")
		else:
			print("you cannot have drivers' license")
	elif country == 'America':
		if age >= 16:
			print("you can have drivers' license")
		else:
			print("you cannot have drivers' license")
else: 
	print('please type in Taiwan or America')
