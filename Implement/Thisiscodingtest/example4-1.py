n = int(input())
data = list(input().split())

dx = [0,0,-1,1]
dy = [-1,1,0,0]
x, y = 1,1

for d in data :
	if d == 'L' :
		direction = 0
	elif d == 'R' :
		direction = 1
	elif d == 'U' :
		direction = 2
	else :
		direction = 3
	
	nx = x + dx[direction]
	ny = y + dy[direction]

	if nx < 1 or ny < 1 or nx > n or ny > n :
		continue
	x, y = nx, ny

print(nx, ny)