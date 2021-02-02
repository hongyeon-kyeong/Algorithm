s = input()
data = s.split('-')
num = []

for d in data :
	cnt = 0
	a = d.split('+')
	for c in a :
		cnt += int(c)
	num.append(cnt)

sum_value = num[0]
for i in range(1, len(num)) :
	sum_value -= num[i]

print(sum_value)