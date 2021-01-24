import sys
input = sys.stdin.readline
n, m = map(int, input().split())
parent = [0] * (n+1)
unions = []

for i in range(n) :
	data = list(map(int, input().split()))
	for j in range(i+1, n) :
		if data[j] == 1 :
			unions.append((i+1, j+1))

for i in range(1,n+1) :
	parent[i] = i

def find_parent(parent, x) :
	if parent[x] != x :
		parent[x] = find_parent(parent,parent[x])
	return parent[x]

def union_parent(parent, a, b) :
	a = find_parent(parent, a)
	b = find_parent(parent, b)

	if a < b :
		parent[b] = a
	else :
		parent[a] = b
	#print(parent)
	
for union in unions :
	union_parent(parent, union[0], union[1])



spots = list(map(int, input().split()))

res = 'YES'
for i in range(m-1) :
	if find_parent(parent, spots[i]) != find_parent(parent, spots[i+1]):
		res = 'NO'
		break
print(res)

'''
5 4
0 1 0 1 1
1 0 1 1 0
0 1 0 0 0
1 1 0 0 0 
1 0 0 0 0
2 3 4 3
'''