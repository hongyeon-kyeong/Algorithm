'''
from itertools import combinations

n, m = map(int, input().split())
weights = list(map(int, input().split()))
data = [ i for i in range(n)]

count = 0
for a, b in list(combinations(data, 2)) :
	if weights[a] != weights[b] :
		count += 1

print(count)
'''

n, m = map(int, input().split())
data = list(map(int, input().split()))

weights = [0] * (n+1)

for d in data :
	weights[d] += 1

count = 0
for i in range(1, m+1) :
	n -= weights[i]
	count += (weights[i] * n)

print(count)