import sys
input = sys.stdin.readline
import copy
array = [[0] * 4 for _ in range(4)]

for i in range(4) :
	data = list(map(int, input().split()))
	for j in range(4) :
		a, b = data[j*2] , data[j*2+1]-1
		array[i][j] = [a,b]

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,-1,-1,-1,0,1,1,1]

def find_fish(array, index) :
	for i in range(4) :
		for j in range(4) :
			if array[i][j][0] == index :
				return (i, j)
	return None

def turn_left(direction) :
	return (direction+1) % 8

def move_fish(array, now_x, now_y) :
	for i in range(1,17) :
		position = find_fish(array, i)

		if position != None :
			x, y  = position
			direction = array[x][y][1]

			for j in range(8) :
				nx = x + dx[direction]
				ny = y + dy[direction]

				if 0 <= nx and 0 <= ny and nx < 4 and ny < 4 :
					if nx != now_x or ny != now_y :
						array[nx][ny] , array[x][y] = array[x][y], array[nx][ny]
						array[nx][ny][1] = direction
						break
				direction = turn_left(direction)

def get_possible_position(array, now_x, now_y) :
	#print('now_x : ', now_x, 'now_y', now_y)
	positions = []
	direction = array[now_x][now_y][1]
	#print('direction : ', direction )

	for i in range(4) :	
		now_x += dx[direction]
		now_y += dy[direction]

		if 0 <= now_x and now_x < 4 and 0 <= now_y and now_y < 4 :
			if array[now_x][now_y][0] != -1 :
				positions.append((now_x, now_y))
	return positions

result = 0	
def dfs(array, now_x, now_y, total) :
	global result
	array = copy.deepcopy(array)
	total += array[now_x][now_y][0]
	array[now_x][now_y][0] = -1
	#print('total : ', total)

	move_fish(array, now_x, now_y)

	positions = get_possible_position(array, now_x, now_y)
	#print('positions : ', positions)

	if len(positions) == 0 :
		result = max(result, total)
		return result
	else :
		for next_x, next_y in positions :
			dfs(array, next_x, next_y, total)

dfs(array, 0,0,0)
print(result)

