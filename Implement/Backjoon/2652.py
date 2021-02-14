max_value = 0
for i in range(9) :
	d = int(input())
	if max_value < d :
		max_value = d
		answer = i

print(max_value)
print(answer+1)