import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M) :
	a, b = map(int, input().split())
	graph[a].append((b,1))
	graph[b].append((a,1))

X, K = map(int, input().split())
distance = [INF] * (N+1)

def dijkstra(start) :
	h = []
	heapq.heappush(h, (0,start))
	
	while h :
		dist, now = heapq.heappop(h)
		if distance[now] < dist :
			continue
		for i in graph[now] :
			cost = dist + i[1]
			if cost < distance[i[0]] :
				distance[i[0]] = cost
				heapq.heappush(h, (cost, i[0]))

dijkstra(1)
A = distance[K]
distance = [INF] * (N+1)
dijkstra(K)
B = distance[X]

if A == INF or B == INF :
	print(-1)
else :
	print(A + B)

'''
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5

4 2
1 3
2 4
3 4
'''