from collections import deque

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(x, y):
    q = deque()
    q.append((x, y, 0))
    graph[x][y] = 1

    while q:
        x, y, w = q.popleft()
        if x == n - 1 and y == m - 1:
            break
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and w == 0:
                    q.append((nx, ny, 1))
                    graph[nx][ny] = graph[x][y] + 1
                elif graph[nx][ny] == 0:
                    q.append((nx, ny, w))
                    graph[nx][ny] = graph[x][y] + 1


bfs(0, 0)
for i in range(n):
    for j in range(m):
        print(graph[i][j], end=' ')
    print()

if graph[n - 1][m - 1] == 0:
    print(-1)
else:
    print(graph[n - 1][m - 1])

# 반례 !
# 5 5
# 00011
# 00011
# 10011
# 00111
# 00010