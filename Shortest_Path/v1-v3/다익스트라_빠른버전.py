import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
s = int(input())

graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m) :
	a, b, c = map(int, input().split())
	graph[a].append((b,c))


def dijkstra(start) :
	h = []
	distance[start]=0
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

dijkstra(s)

for i in range(1,n+1) :
	if distance[i] == INF :
		print("INFINITY")
	else :
		print(distance[i])