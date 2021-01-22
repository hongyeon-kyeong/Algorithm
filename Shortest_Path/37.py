import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[100001 for _ in range(n+1)] for _ in range(n+1)]

#for i in range(1,n+1) :
#	graph[i][i] = 0

for _ in range(m) :
	a, b, c = map(int,input().split())
	graph[a][b] = c

for i in range(1,n+1):
	for j in range(1,n+1) :
		if j == i :
			continue
		for k in range(1,n+1) :
			if k == i or k == j :
				continue
			graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])

for i in range(1,n+1) :
	for j in range(1, n+1) :
		print(graph[i][j], end=' ')
	print()