def factorial(n) :
	value = 1
	for i in range(n, 1, -1) :
		value *= i
	return value

def factorial2(n) :
	if n <= 1 :
		return 1
	else :
		return n * factorial(n-1)

print("1 : ", factorial(5))
print("2 : ", factorial2(5))
