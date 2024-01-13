import heapq
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
INF = int(1e9)
distance = [INF] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((1, b))
    graph[b].append((1, a))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[0]
            if cost < distance[i[1]]:
                distance[i[1]] = cost
                heapq.heappush(q, (cost, i[1]))

dijkstra(1)
result_node = 0
result_distance = -1
same_node = 0
for i in range(1, n+1):
    if result_distance < distance[i]:
        result_distance = distance[i]
        result_node = i
        same_node = 0
    if result_distance == distance[i]:
        same_node += 1
print(result_node, result_distance, same_node, end=' ')
