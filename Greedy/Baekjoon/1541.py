s = input()
data = list(s.split('-'))
res = 0

for i in range(len(data)) :
	sum = 0
	if i == 0 :
		if '+' in data[i] :
			data_2 = list(data[i].split('+'))
			for d2 in data_2 :
				sum += int(d2)
		else :
			sum = int(data[i])
		res += sum
	else :
		if '+' in data[i] :
			data_2 = list(data[i].split('+'))
			for d2 in data_2 :
				sum += int(d2)
		else :
			sum = int(data[i])
		res -= sum

print(res)
