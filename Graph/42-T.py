import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
parent = [0] * (n+1)

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

for i in range(1,n+1) :
	parent[i] = i

count = 0 
gates = []
for _ in range(m) :
	gates.append(int(input()))

for gate in gates :
	par = find_parent(parent, gate)
	if par == 0 :
		break
	else :
		union_parent(parent, par, par-1)
		count += 1

print(count)