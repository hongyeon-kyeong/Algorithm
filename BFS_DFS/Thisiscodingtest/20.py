from itertools import combinations
n = int(input())
board = []
teachers = []
spaces = []

for i in range(n) :
	data = list(input().split())
	board.append(data)
	for j in range(n) :
		if data[j] == 'T' :
			teachers.append((i, j))
		if data[j] == 'X' :
			spaces.append((i,j))

def watch(x,y,direction) :
	if direction == 0 :
		while y >= 0 :
			if board[x][y]  == 'S' :
				return True
			if board[x][y] == 'O' :
				return False
			y -= 1
	elif direction == 1 :
		while y < n :
			if board[x][y]  == 'S' :
				return True
			if board[x][y] == 'O' :
				return False
			y += 1
	elif direction == 2 :
		while x >= 0 :
			if board[x][y]  == 'S' :
				return True
			if board[x][y] == 'O' :
				return False
			x -= 1
	else :
		while x < n :
			if board[x][y]  == 'S' :
				return True
			if board[x][y] == 'O' :
				return False
			x += 1

def process() :
	for x, y in teachers :
		for i in range(4) :
			if watch(x, y, i) :
				return True
	return False

find = False
for space in combinations(spaces, 3) :
	for x, y in space :
		board[x][y] = 'O'
	if not process() :
		find = True
		break
	else :
		for x, y in space :
			board[x][y] = 'X'

if find : 
	print('YES')
else :
	print('NO')
