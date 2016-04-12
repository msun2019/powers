def power(base, exponent):
	if exponent != 0:
		return int(base) * power(base, exponent - 1)
	else:	
		return 1
		

	
	

	


	
print(power(3,1))