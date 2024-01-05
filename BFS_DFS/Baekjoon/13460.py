from collections import deque

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(input()))
    for j in range(m):
        if graph[i][j] == 'R':
            rx, ry = i, j
        elif graph[i][j] == 'B':
            bx, by = i, j
visited = [[[[False] * m for i in range(n)] for _ in range(m)] for _ in range(n)]

# 상, 하, 좌,
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

bq = deque()
bq.append((bx, by))
rq = deque()
rq.append((rx, ry, 0))
visited[rx][ry][bx][by] = True

chk = False


def move(x, y, d):
    cnt = 0
    while True:
        nx = x + dx[d]
        ny = y + dy[d]
        if graph[nx][ny] != '#' and graph[x][y] != 'O':
            x, y = nx, ny
            cnt += 1
        else:
            break
    return x, y, cnt


while bq and rq:
    bx, by = bq.popleft()
    rx, ry, count = rq.popleft()

    if count+1 > 10:
        break
    #print(rx, ry, bx, by, count)
    for i in range(4):
        nrx, nry, rcnt = move(rx, ry, i)
        nbx, nby, bcnt = move(bx, by, i)

        if graph[nbx][nby] != 'O':
            if graph[nrx][nry] == 'O':
                chk = True
                break
            if nrx == nbx and nry == nby:
                if rcnt > bcnt:
                    nrx -= dx[i]
                    nry -= dy[i]
                else:
                    nbx -= dx[i]
                    nby -= dy[i]

            if not visited[nrx][nry][nbx][nby]:
                visited[nrx][nry][nbx][nby] = True
                rq.append((nrx, nry, count + 1))
                bq.append((nbx, nby))
    if chk:
        break

if not chk:
    print(-1)
else:
    print(count+1)
