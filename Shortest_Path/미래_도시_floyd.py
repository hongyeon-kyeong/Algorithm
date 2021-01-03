import sys
input = sys.stdin.readline
INF = int(1e9)

N, M = map(int, input().split())

graph = [[INF for _ in range(N+1)] for _ in range(N+1)]
for _ in range(M) :
	a, b = map(int, input().split())
	graph[a][b] = 1
	graph[b][a] = 1

for i in range(1,N+1) :
	graph[i][i] = 0

X, K = map(int, input().split())

for i in range(1, N+1) :
	for j in range(1, N+1) :
		for k in range(1, N+1) :
			graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])

if graph[1][K] == INF or graph[K][X] == INF :
	print(-1)
else :
	print(graph[1][K] + graph[K][X])
