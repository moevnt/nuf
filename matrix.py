x = 0
y = 0
z = 0

print("All values are 0 to 10")


def get_x():
	body = int(input("Is she Hot(10) or ugly(0): "))
	return body
	
	
def get_y():
	alcohol = int(input("Are you Sober(10) or Drunk(0): "))
	return alcohol
	
	
def get_z():
	personality = int(input("Is she Cool(10) or Crazy(0): "))
	return personality


x = get_x()
y = get_y()
z = get_z()


def odds():
	average = (x+y+z)/3
	odds = (10*average)
	return odds


# Big No = ugly, sober, crazy 0%
# No = ugly, sober, cool
# Nah? = ugly, drunk, crazy

# Maybe1 = hot, sober, crazy
# Maybe = ugly, drunk, cool
# Maybe = 0,0,0 50%

# Yes = hot, drunk, crazy
# Absolutely yes = hot, drunk, cool
# Hell yes = hot, sober, cool 100%

odds = odds()
print(odds)


def decide1(odds):
	if 44.5 < odds > 55.5:
		return 'Maybe'
	elif 66.5 > odds > 55.5:
		return 'Yes'
	elif 66.5 < odds < 77.5:
		return 'Absolutely Yes'
	elif 77.7 < odds:
		return 'Hell yes'
	elif 44.5 > odds > 33.5:
		return 'Nah?'
	elif 33.5 > odds > 22.5:
		return 'No'
	elif 22.5 > odds:
		return 'Big No'

	
def decide():
	if (x == 5 & y==5 & z==5):
		return 'Maybe'
	
	if (x > 5):
		if(y > 5):
			if(z > 5):
				return 'Hell Yes'
			else:
				return 'Yes'
		else:
			if(z > 5):
				return 'Absolutely Yes'
			else:
				return 'Maybe1'
	else:
		if (y > 5):
			if (z > 5):
				return 'No'
			else:
				return 'Big No'
		else:
			if (z > 5):
				return 'Maybe'
			else:
				return 'Nah?'


print(decide1(odds))
