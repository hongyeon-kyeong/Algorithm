import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m, c = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m) :
	x, y, z = map(int, input().split())
	graph[x].append((y,z))

distance = [INF] * (n+1)

def dijkstra(start) :
	h = []
	heapq.heappush(h, (0, start))
	distance[start] = 0

	while h :
		dist, now = heapq.heappop(h)
		#print(dist, now)
		if distance[now] < dist :
			continue
		for i in graph[now] :
			cost = dist + i[1]
			if cost < distance[i[0]] :
				distance[i[0]] = cost
				heapq.heappush(h, (cost, i[0]))

dijkstra(c)

count = 0
max_distance = 0
print(distance)
for i in range(1, n+1) :
	if distance[i] != INF and i != c :
		count += 1
		#if max < distance[i] :
		#	max = distance[i]
		max_distance = max(max_distance, distance[i])
print(count, max_distance)

'''
3 2 1
1 2 4
1 3 2
'''