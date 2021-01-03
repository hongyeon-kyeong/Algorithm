import sys
input = sys.stdin.readline

def find_parent(parent, x) :
	if parent[x] != x :
		parent[x] = find_parent(parent, parent[x])
	return parent[x]

def union_parent(parent, a, b) :
	a = find_parent(parent, a) 
	b = find_parent(parent, b)

	if a < b :
		parent[b] = a
	else :
		parent[a] = b

v, e = map(int, input().split())
parent = [0] * (v+1)

for i in range(1,v+1) :
	parent[i] = i

edges = []
for _ in range(e) :
	a, b, cost = map(int, input().split())
	edges.append((cost, a, b))

edges.sort()
result = 0

for i in edges :

	# cost, a, b = egde

	a = find_parent(parent, i[1]) 
	b = find_parent(parent, i[2])

	if a != b :
		result += i[0]
		union_parent(parent, i[1],i[2])

print(result)

'''
7 9
1 2 29
1 5 75
2 3 35
2 6 34
3 4 7
4 6 23
4 7 13
5 6 53
6 7 25
'''