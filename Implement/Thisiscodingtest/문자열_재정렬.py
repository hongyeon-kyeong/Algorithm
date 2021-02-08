s = input()
result = []
#print(ord('A'))
sum_value = 0
for data in s :
	if ord(data) >= ord('A') :
		result.append(data)
	else :
		sum_value += int(data)

result.sort()
## 합이 0인 경우도 생각해주기!
if sum_value != 0 :
	result.append(str(sum_value))

print(''.join(result))
