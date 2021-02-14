n, m = map(int, input().split())
x, y, d = map(int, input().split())
array = []
for _ in range(n) :
	array.append(list(map(int, input().split())))

dx = [-1,0,1,0]
dy = [0,-1,0,1]

def turn_left() :
	global d
	d += 1
	if d == 4 :
		d = 0

turn_count = 0
count = 0
while True :
	turn_left()
	turn_count += 1

	nx = x + dx[d]
	ny = y + dy[d]

	if array[nx][ny] == 0 :
		array[nx][ny] = 2
		x, y = nx, ny
		count+=1
		turn_count = 0

	else :
		turn_left()
		turn_count += 1

		if turn_count >= 4 :
			nx = x - dx[d]
			ny = y - dy[d]
			if array[nx][ny] == 1 :
				break
			else :
				array[nx][ny] = 2
				x, y = nx, ny
				turn_count = 0
print(count)

'''
4 4
1 1 0
1 1 1 1 
1 0 0 1
1 1 0 1 
1 1 1 1 
'''

