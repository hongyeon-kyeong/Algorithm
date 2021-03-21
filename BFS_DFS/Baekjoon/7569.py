import sys
from collections import deque
input = sys.stdin.readline().rstrip()
m, n, h = map(int, input.split())
graph = []
q = deque()
tomato = 0
count = 0
visited = [[[False for _ in range(m)] for _ in range(n)] for _ in range(h)]
for i in range(h) :
    data = []
    for j in range(n) :
        data.append(list(map(int,  sys.stdin.readline().rstrip().split())))
        for k in range(m) :
            if data[j][k] == 1 :
                q.append((i, j, k))
                visited[i][j][k] = True
            elif data[j][k] == 0 :
                tomato += 1
    graph.append(data)

while q and tomato:
    for _ in range(len(q)):
        z, x, y = q.popleft()
        if z + 1 < h and graph[z+1][x][y] == 0:
            graph[z+1][x][y] = 1
            q.append((z+1, x, y))
            tomato -= 1
        if z > 0 and graph[z-1][x][y] == 0:
            graph[z-1][x][y] = 1
            q.append((z-1, x, y))
            tomato -= 1
        if x + 1 < n and graph[z][x+1][y] == 0:
            graph[z][x+1][y] = 1
            q.append((z, x+1, y))
            tomato -= 1
        if x > 0 and graph[z][x-1][y] == 0:
            graph[z][x-1][y] = 1
            q.append((z, x-1, y))
            tomato -= 1
        if y + 1 < m and graph[z][x][y+1] == 0:
            graph[z][x][y+1] = 1
            q.append((z, x, y+1))
            tomato -= 1
        if y > 0 and graph[z][x][y-1] == 0:
            graph[z][x][y-1] = 1
            q.append((z, x, y-1))
            tomato -= 1
    count += 1

if tomato:
    print(-1)
else:
    print(count)