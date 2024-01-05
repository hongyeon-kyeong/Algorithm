n, m = map(int, input().split())
loc_x, loc_y, direction = map(int, input().split())

d = [[0] * m for _ in range(n)]

array = []
for _ in range(n):
    array.append(list(map(int, input().split())))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def rotate():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

count = 1
d[loc_x][loc_y] = 1
turn_time = 0

while True:
    rotate()

    nx = loc_x + dx[direction]
    ny = loc_y + dy[direction]

    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        count += 1
        loc_x = nx
        loc_y = ny
        turn_time = 0
        continue
    else:
        turn_time += 1
    if turn_time == 4:
        nx = loc_x - dx[direction]
        ny = loc_y - dy[direction]
        if array[nx][ny] == 0:
            loc_x = nx
            loc_y = ny
        else:
            break
        turn_time = 0

print(count)













