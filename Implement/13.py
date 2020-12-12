
import sys
from itertools import combinations
N, M = map(int, sys.stdin.readline().rstrip().split())
houses = list()
chickens = list()
cities = list()
for i in range(N) :
	cities.append(list(map(int, sys.stdin.readline().rstrip().split())))
	for j in range(N) :
		if cities[i][j] == 1 :
			houses.append([i,j])
		elif cities[i][j] == 2 :
			chickens.append([i,j])

selected_chicks = list(combinations(chickens,M))

def distance(house, chi) :
	r1 = house[0]
	c1 = house[1]
	r2 = chi[0]
	c2 = chi[1]

	return abs(r1-r2) + abs(c1-c2)

res = 50 * 2 * N
for chicks in selected_chicks :
	sum = 0
	for house in houses :
		min_value = 2 * N
		for chi in chicks :
			dist = distance(house, chi)
			min_value = min(min_value, dist)
		sum += min_value
	res = min(res, sum)

print(res)



