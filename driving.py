country = input('What country are you from(type in Taiwan or America):') 
age = int(input('how old are you:'))
if country == Taiwan:
	if age <= 18:
		print('you can have driver license')
	else:
		print('you cannot have driver license')
