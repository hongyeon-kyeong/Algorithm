n, m = map(int, input().split())
array = []
for i in range(n):
    array.append(list(map(int, input())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
result = 0

def make_ice(x, y):
    global array
    array[x][y] = 2
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if nx >= 0 and ny >= 0 and nx < n and ny < m:
            if array[nx][ny] == 0:
                make_ice(nx, ny)

for i in range(n):
    for j in range(m):
        if array[i][j] == 0:
            make_ice(i, j)
            result += 1

print(result)