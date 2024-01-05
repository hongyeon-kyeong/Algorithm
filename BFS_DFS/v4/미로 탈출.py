n, m = map(int, input().split())
array = [[0] * m for _ in range(n)]
for i in range(n):
    array[i] = list(map(int, input()))

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, count):
    global array
    array[x][y] = count + 1

    if x == n-1 and y == m-1:
        return

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if nx >= 0 and ny >= 0 and nx < n and ny < m:
            if array[nx][ny] == 1:
                dfs(nx, ny, array[x][y])

dfs(0, 0, 1)
print(array[n-1][m-1]-1)
