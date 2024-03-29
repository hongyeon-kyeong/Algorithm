import heapq
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
INF = int(1e9)
distance = [INF] * (n+1)
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

X, K = map(int, input().split())
dijkstra(1)
A = distance[K]
distance = [INF] * (n+1)
dijkstra(K)
B = distance[X]

if A == INF or B == INF:
    print(-1)
else:
    print(A+B)

