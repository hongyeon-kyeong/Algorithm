import heapq
import sys
input = sys.stdin.readline

N, M, C = map(int, input().split())
INF = int(1e9)
distance = [INF] * (N+1)
graph = [[] for _ in range(N+1)]
for i in range(M):
    X, Y, Z = map(int, input().split())
    graph[X].append((Y, Z))

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(C)
count = 0
time = 0
for i in range(1, N+1):
    if distance[i] < INF:
        count += 1
        time = max(time, distance[i])
print(count-1)
print(time)


