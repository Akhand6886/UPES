

def primeno(number):
	flag = False

	for i in range(2,number):
		if (number%i)==0:
			flag = True
		break 

	if flag: 
		return False
	else:
		return True

print(primeno(3))