n = int(input())
data = list(map(int, input().split()))

data.sort()
num = 0
result = 0

for i in range(n) :
	num += 1
	if num == data[i] :
		result += 1
		num = 0

print(result)
