import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m) :
	a, b = map(int, input().split())
	graph[a].append(b)
	graph[b].append(a)

def dijkstra(start) :
	h = []
	heapq.heappush(h, (0,start))
	distance[start] = 0

	while h :
		dist , now = heapq.heappop(h)

		for v in graph[now] :
			cost = dist + 1

			if cost < distance[v] :
				distance[v] = cost
				heapq.heappush(h, (cost, v))

dijkstra(1)

res = 0
res_node = 0
result = []
for i in range(1,n+1) :
	if res < distance[i] :
		res = distance[i]
		res_node = i
		result = [res_node]
	elif res == distance[i] :
		result.append(i)


'''
for i in range(1,n+1) :
	if res == distance[i] :
		count += 1
'''

print(res_node, res, len(result))

'''
6 7
3 6
4 3
3 2
1 3
1 2
2 4
5 2
'''
