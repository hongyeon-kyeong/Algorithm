n, m = map(int, input().split())
data = list(map(int, input().split()))

weights = [0] * (n+1)
for i in range(n) :
	weights[data[i]] += 1

count = 0
for i in range(1, m+1) :
	n -= weights[i]
	count += (weights[i] * n)

print(count)

# 횟수단축