
data = [-1] * 10001
def func(num) :
	if num > 10001 :
		return

	sum_value = num
	for n in str(num) :
		sum_value += int(n)

	if sum_value < 10001 and data[sum_value] == -1 :
		data[sum_value] = num
		func(sum_value)

for i in range(1, 10001) :
	func(i)

#print(data)
for i in range(1, 10001) :
	if data[i] == -1 :
		print(i)