s = input()
sum = 0
for d in s :
	if sum <= 1 or int(d) <= 1 :
		sum += int(d)
	else :
		sum *= int(d)
print(sum)