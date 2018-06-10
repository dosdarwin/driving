country = input('What country are you from(type in Taiwan or America):') 
age = int(input('how old are you:'))
if country == 'Taiwan':
	if age >= 18:
		print("you can have drivers' license")
	else:
		print("you cannot have drivers' license")
if country == 'America':
	if age >= 16:
		print("you can have drivers' license")
	else:
		print("you cannot have drivers' license")