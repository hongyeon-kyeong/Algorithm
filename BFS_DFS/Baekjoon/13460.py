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

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
print('rx :', rx, 'ry : ', ry, 'bx : ', bx, 'by : ', by)

bq = deque()
bq.append((bx, by))
rq = deque()
rq.append((rx, ry, 0))
chk = False
while bq and rq:
    bx, by = bq.popleft()
    rx, ry, count = rq.popleft()

    for i in range(4):
        bnx = bx + dx[i]
        rnx = rx + dx[i]
        bny = by + dy[i]
        rny = ry + dy[i]

        # 파란 구슬 이동
        if graph[bnx][bny] == 'O':
            continue
        elif graph[bnx][bny] != '#':
            bq.append((bnx, bny))
            graph[bx][by] = '.'

        # 빨간 구슬 이동
        if graph[rnx][rny] == 'O':
            chk = True
            break
        elif graph[rnx][rny] != '#':
            rq.append((rnx, rny, count+1))
            graph[rx][ry] = '.'
    if chk:
        break

if count+1 > 10:
    print(-1)
else:
    print(count+1)