n, m = map(int, input().split())
result = 0
for _ in range(n) :
	data = list(map(int, input().split()))
	result = max(result, min(data))

print(result)

result = 0
for _ in range(n) :
	data = list(map(int, input().split()))
	
	min_value = 10001
	
	for d in data :
		min_value = min(min_value, d)
	
	result = max(result, min_value)

print(result)
