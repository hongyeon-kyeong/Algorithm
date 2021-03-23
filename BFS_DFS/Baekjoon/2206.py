from collections import deque

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

visited = [[[0, 0] for _ in range(m)] for _ in range(n)]

def bfs(x, y):
    q = deque()
    q.append((x, y, 0))
    visited[x][y][0] = 1

    while q:
        x, y, w = q.popleft()
        if x == n - 1 and y == m - 1:
            return visited[x][y][w]
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and w == 0:
                    q.append((nx, ny, 1))
                    visited[nx][ny][1] = visited[x][y][w] + 1
                elif visited[nx][ny][w] == 0 and graph[nx][ny] == 0:
                    q.append((nx, ny, w))
                    visited[nx][ny][w] = visited[x][y][w] + 1
    return 0


answer = bfs(0, 0)

if answer == 0:
    print(-1)
else:
    print(answer)

# 반례 !
# 5 5
# 00011
# 00011
# 10011
# 00111
# 00010