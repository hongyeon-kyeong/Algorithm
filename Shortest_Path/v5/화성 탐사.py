import heapq
t = int(input())
INF = int(1e9)
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
start = (0, 0)
for _ in range(t):
    n = int(input())
    graph = [[] * n for _ in range(n)]
    distance = [[INF] * n for _ in range(n)]
    for i in range(n):
        graph[i] = list(map(int, input().split()))

    q = []
    heapq.heappush(q, (graph[start[0]][start[1]], start))
    distance[start[0]][start[1]] = graph[start[0]][start[1]]
    while q:
        dist, now = heapq.heappop(q)
        if distance[now[0]][now[1]] < dist:
            continue
        for i in range(4):
            nx = dx[i] + now[0]
            ny = dy[i] + now[1]
            if nx >= 0 and ny >= 0 and nx < n and ny < n:
                cost = dist + graph[nx][ny]
                if cost < distance[nx][ny]:
                    distance[nx][ny] = cost
                    heapq.heappush(q, (cost, (nx, ny)))
    print(distance[n-1][n-1])