n = int(input())
for _ in range(n) :
	sum_value = 0
	index = 1
	data = input()
	for d in data :
		if d == 'O' :
			sum_value += index
			#print(d, index, sum_value)
			index += 1
		else :
			index = 1
	print(sum_value)