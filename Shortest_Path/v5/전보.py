import heapq
n, m, c = map(int, input().split())
graph = [[] for _ in range(n+1)]
INF = int(1e9)
distance = [INF] * (n+1)

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((z, y))

start = c
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

dijkstra(start)
city = -1
time = 0
for i in range(1, n+1):
    if distance[i] == INF:
        continue
    city += 1
    time = max(time, distance[i])

print(city, end=" ")
print(time)