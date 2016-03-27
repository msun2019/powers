def power(base, power):
	if power == 0:
		answer = 1
	else:
		list = []
		looper = power
		answer = base
		while looper != 1:
			list.append("Value") 
			looper -= 1
		for item in list:
			answer= answer * base
	print(answer)
	
power(4,0)