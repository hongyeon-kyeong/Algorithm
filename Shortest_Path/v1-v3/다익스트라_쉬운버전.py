import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
cost = [INF] * (n+1)
s = int(input())
for i in range(m) :
	n1, n2, c = map(int, input().split())

	graph[n1].append((n2,c))

def get_smallest() :
	min_value = INF
	res = 0

	for i in range(1,n+1) :
		if not visited[i] :
			if cost[i] < min_value :
				min_value = cost[i]
				res = i
	return res

def dijkstra(s) :
	cost[s] = 0
	visited[s] = True

	for v, c in graph[s] :
		cost[v] = min(cost[v], c)

	for i in range(n-1) :
		cur = get_smallest()
		visited[cur] = True

		for v,c in graph[cur] :
				cost[v] = min(cost[v],  cost[cur]+c)

dijkstra(s)

for i in range(1,n+1) :
	if cost[i] == INF :
		print("INFINITY")
	else :
		print(cost[i])