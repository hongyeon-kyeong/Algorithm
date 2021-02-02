s = input()
result = 0
for d in s :
	if int(d) <= 1 or result <= 1 :
		result += int(d)
	else :
		result *= int(d)

print(result)

# 곱하거나 더하는 값을 최대로 만들기 위해서는 0,1일 때는 더하는 게 유리, 이외에는 곱하는게 유리하다.