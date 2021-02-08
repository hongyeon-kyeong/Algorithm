n,m = map(int, input().split())
x, y, d = map(int, input().split())
array = []
for _ in range(n) :
	array.append(list(map(int, input().split())))
data = [[0]*m for _ in range(n)]
data[x][y] = 1

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def turn_left() :
	global d
	d -= 1
	if d == -1 :
		d = 3

count = 1
turn_count = 0
while True :

	turn_left()
	nx = x + dx[d]
	ny = y + dy[d]

	if data[nx][ny] == 0 and array[nx][ny] == 0 :
		data[nx][ny] = 1
		count += 1
		turn_count = 0
		x, y = nx, ny
	else :
		turn_count += 1
		if turn_count == 4 :
			nx = x - dx[d]
			ny = y - dy[d]

			if array[nx][ny] == 0 :
				x, y = nx, ny
				turn_count = 0
			else :
				break
print(count)
