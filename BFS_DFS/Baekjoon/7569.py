import sys
import heapq
input = sys.stdin.readline().rstrip()
m, n, h = map(int, input.split())
graph = []
q = []
tomato = 0
count = 0
visited = [[[False for _ in range(m)] for _ in range(n)] for _ in range(h)]
for i in range(h) :
    data = []
    for j in range(n) :
        data.append(list(map(int,  sys.stdin.readline().rstrip().split())))
        for k in range(m) :
            if data[j][k] == 1 :
                heapq.heappush(q, (count, i, j, k))
                visited[i][j][k] = True
            elif data[j][k] == 0 :
                tomato += 1
    graph.append(data)

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

# while q and tomato:
#     count, z, x, y = heapq.heappop(q)
#     for d in range(6):
#         nx = x + dx[d]
#         ny = y + dy[d]
#         nz = z + dz[d]
#         if nx >= 0 and ny >= 0 and nz >= 0 and nx < n and ny < m and nz < h :
#             if graph[nz][nx][ny] == 0 and visited[nz][nx][ny] == False :
#                 graph[nz][nx][ny] = 1
#                 visited[nz][nx][ny] = True
#                 tomato -= 1
#                 heapq.heappush(q, (count+1, nz, nx, ny))

while q and tomato:
    count, z, x, y = heapq.heappop(q)
    next_tomato = 0
    if z + 1 < h and graph[z+1][x][y] == 0:
        graph[z+1][x][y] = 1
        heapq.heappush(q, (count+1, z+1, x, y))
        tomato -= 1
        next_tomato += 1
    if z > 0 and graph[z-1][x][y] == 0:
        graph[z-1][x][y] = 1
        heapq.heappush(q, (count+1, z-1, x, y))
        tomato -= 1
        next_tomato += 1
    if x + 1 < n and graph[z][x+1][y] == 0:
        graph[z][x+1][y] = 1
        heapq.heappush(q, (count+1, z, x+1, y))
        tomato -= 1
        next_tomato += 1
    if x > 0 and graph[z][x-1][y] == 0:
        graph[z][x-1][y] = 1
        heapq.heappush(q, (count+1, z, x-1, y))
        tomato -= 1
        next_tomato += 1
    if y + 1 < m and graph[z][x][y+1] == 0:
        graph[z][x][y+1] = 1
        heapq.heappush(q, (count+1, z, x, y+1))
        tomato -= 1
        next_tomato += 1
    if y > 0 and graph[z][x][y-1] == 0:
        graph[z][x][y-1] = 1
        heapq.heappush(q, (count+1, z, x, y-1))
        tomato -= 1
        next_tomato += 1
    if next_tomato > 0:
        count += 1
if tomato:
    print(-1)
else:
    print(count)