n, m = map(int, input().split())
a, b, d = map(int, input().split())

# 방문여부를 기록
data = [[0]*m for _ in range(n)]
array = []
for _ in range(n) :
	array.append(list(map(int, input().split())))

dx = [-1,0,1,0]
dy = [0,1,0,-1]
data[a][b] = 1

def rotate() :
	global d
	d -= 1
	if d == -1 :
		d = 3

count = 1
turn_count = 0
while True :
	
	rotate()
	nx = a + dx[d]
	ny = b + dy[d]

	if array[nx][ny] == 0 and data[nx][ny] == 0 :
		data[nx][ny] = 1
		turn_count = 0
		a, b = nx, ny
		count += 1
		continue
	else :
		turn_count +=1

		if turn_count == 4 :
			nx = a + dx[d]*-1
			ny = a + dy[d]*-1

			if array[nx][ny] != 1 :
				a, b = nx, ny
			else :
				break
			turn_count = 0

print(count)
		

