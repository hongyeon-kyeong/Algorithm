import sys
input = sys.stdin.readline

N, M = map(int, input().split())
parent = [0] * (N+1)

for i in range(1, N+1) :
	parent[i] = i

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

for _ in range(M) :
	t, a, b = map(int, input().split())

	if t == 0 :
		union_parent(parent, a, b)
	else :
		parent_a = find_parent(parent, a)
		parent_b = find_parent(parent, b)

		if parent_a == parent_b :
			print('YES')
		else :
			print('NO')