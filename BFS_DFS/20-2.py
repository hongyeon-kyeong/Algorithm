import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())
graph = []
teachers = []
temp = [[0]*n for _ in range(n)]
dx = [1,-1,0,0]
dy = [0,0,-1,1]

for i in range(n) :
	graph.append(list(input().split()))

for i in range(n) :
	for j in range(n) :
		if graph[i][j] == 'X' :
			teachers.append((i, j))

def watch(x, y, temp, k) :
	nx = x + dx[k]
	ny = y + dy[k]

	if 0 <= nx and 0 <= ny and nx < n and ny < n :
		if temp[nx][ny] == 'X' :
			return watch(nx, ny, temp, k)
		elif temp[nx][ny] == 'S' :
			return False
	else :
		return True
		
for teacher in list(combinations(teachers,3)) :
	check = True
	for i in range(n) :
		for j in range(n) :
			temp[i][j] = graph[i][j]
			
	for t in teacher :
		x, y = t
		temp[x][y] = 'O'

	for i in range(n) :
		for j in range(n) :
			if temp[i][j] == 'T' :
				for k in range(4) :
					if watch(i, j, temp, k) == False :
						check = False
	if check :
		break

if check :
	print('YES')
else :
	print('NO')
	

