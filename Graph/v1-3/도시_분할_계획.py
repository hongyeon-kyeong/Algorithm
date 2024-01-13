import sys
input = sys.stdin.readline

N, M = map(int, input().split())
parent = [0] * (N+1)
count  = 0

def find_parent(parent, x) :
	if parent[x] != x :
		parent[x] = find_parent(parent, parent[x])
	return parent[x]

def union_parent(parent, a, b) :
	a = find_parent(parent, a)
	b = find_parent(parent, b)

	global count
	count += 1
	
	if a < b :
		parent[b] = a
	else :
		parent[a] = b

for i in range(1, N+1) :
	parent[i] = i

edges = []
for _ in range(M) :
	a, b, cost = map(int, input().split())
	edges.append((cost, a, b))

edges.sort()
result = 0

for edge in edges :
	cost, a, b = edge

	if count == N-2 :
		print(result)
		break

	if find_parent(parent, a) != find_parent(parent, b) :
		union_parent(parent, a, b)
		result += cost

'''
7 12
1 2 3
1 3 2
3 2 1
2 5 2
3 4 4
7 3 6
5 1 5
1 6 2
6 4 1
6 5 3
4 5 3
6 7 4
'''