n = int(input())
data = list(map(int, input().split()))
sum = 0
result = 0

data.sort()

for i in range(n) :
	sum += data[i]
	result += sum

print(result)
