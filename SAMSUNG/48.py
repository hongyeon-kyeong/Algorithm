n, m, k = map(int, input().split())

array = []
for i in range(n) :
	array.append(list(map(int, input().split())))

directions = list(map(int, input().split()))

smell = [[[0,0]]*n for _ in range(n)]

priorites = [[] for _ in range(m)]

for i in range(m) :
	for j in range(4) :
		priorites[i].append(list(map(int, input().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def update_smell() :
	for i in range(n) :
		for j in range(n) :
			if smell[i][j][1] > 0 :
				smell[i][j][1] -= 1

			if array[i][j] != 0 :
				smell[i][j] = [array[i][j], k]

def move() :
	new_array = [[0] * n for _ in range(n)]

	for x in range(n) :
		for y in range(n) :
			if array[x][y] != 0 :
				direction = directions[array[x][y] -1]
				found = False
				for index in range(4) :
					nx = x + dx[priorites[array[x][y]-1]]