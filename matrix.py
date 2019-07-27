x = 0
y = 0
z = 0

print("All values are -10 to 10")


def get_x():
	body = int(input("Hot(10) or ugly(-10): "))
	return body
	
	
def get_y():
	alcohol = int(input("Drunk(10) or sober(-10): "))
	return alcohol
	
	
def get_z():
	personality = int(input("cool(10) or crazy(-10): "))
	return personality


x = get_x()
y = get_y()
z = get_z()

# Big No = ugly, sober, crazy 0%
# No = ugly, sober, cool
# Nah? = ugly, drunk, crazy

# Maybe1 = hot, sober, crazy
# Maybe = ugly, drunk, cool
# Maybe = 0,0,0 50%

# Yes = hot, drunk, crazy
# Absolutely yes = hot, drunk, cool
# Hell yes = hot, sober, cool 100%


def odds():
	average = (x+y+z)/3
	odds = (10*average)
	return odds

print(odds())
	
	
def decide():
	if (x == 0):
		return 'Maybe'
	
	if (x > 0):
		if(y > 0):
			if(z > 0):
				return 'Hell Yes'
			else:
				return 'Yes'
		else:
			if(z > 0):
				return 'Absolutely Yes'
			else:
				return 'Maybe1'
	else:
		if (y > 0):
			if (z > 0):
				return 'No'
			else:
				return 'Big No'
		else:
			if (z > 0):
				return 'Maybe'
			else:
				return 'Nah?'


#print(decide())
