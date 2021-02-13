from itertools import combinations
n, m = map(int, input().split())
array = []
for _ in range(n):
    array.append(list(map(int, input().split())))

houses = []
chiks = []
for i in range(n):
    for j in range(n):
        if array[i][j] == 1:
            houses.append((i + 1, j + 1))
        if array[i][j] == 2:
            chiks.append((i + 1, j + 1))

result = int(1e9)
for chickens in list(combinations(chiks, m)):
    sum_dist = 0
    for r1, c1 in houses:
        min_dist = n * 2
        for r2, c2 in chickens:
            dist = abs(r1 - r2) + abs(c1 - c2)
            min_dist = min(dist, min_dist)
        sum_dist += min_dist
    result = min(sum_dist, result)
print(result)

from itertools import combinations

n, m = map(int, input().split())
chicken, house = [], []

for r in range(n) :
	data = list(map(int, input().split()))
	for c in range(n) :
		if data[c] == 1 :
			house.append((r,c))
		elif data[c] == 2 :
			chicken.append((r,c))

candidates = list(combinations(chicken, m)) 

def get_sum(candidate) :
	result = 0
	for hx, hy in house :
		temp = 1e9
		for cx, cy in candidate :
			temp = min(temp, abs(hx-cx)+abs(hy-cy))
		result += temp
	return result

result = 1e9
for candidate in candidates :
	result = min(result, get_sum(candidate))

print(result)
