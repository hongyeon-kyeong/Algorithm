import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
maps = []

for _ in range(n) :
	maps.append(list(map(int, input().split())))
0
now_size = 2
now_x, now_y = 0,0
for i in range(n) :
	for j in range(n) :
		if maps[i][j] == 9 :
			now_x, now_y = i, j
			maps[i][j] = 0

def bfs() :
	dist = [[-1] * n for _ in range(n)]
	dx = [-1,0,1,0]
	dy = [0,-1,0,1]

	q = deque([(now_x, now_y)])
	dist[now_x][now_y] = 0

	while q :
		x, y = q.popleft()

		for i in range(4) :
			nx = x + dx[i]
			ny = y + dy[i]

			if 0 <= nx and nx < n and 0 <= ny and ny < n :
				if dist[nx][ny] == -1 and maps[nx][ny] <= now_size :
					dist[nx][ny] = dist[x][y]+1
					q.append((nx, ny))
	return dist

def find(dist) :
	x, y = 0, 0
	min_value = int(1e9)

	for i in range(n) :
		for j in range(n) :
			if dist[i][j] != -1 and dist[i][j] < min_value and 0 < maps[i][j] and maps[i][j] < now_size :
				min_value = dist[i][j]
				x, y = i, j
	
	if min_value == int(1e9) :
		return None
	else :
		return x, y, min_value

result = 0
ate = 0 
while True :
	value = find(bfs())

	if value == None :
		print(result)
		break
	else :
		now_x, now_y = value[0], value[1]
		maps[now_x][now_y] = 0
		result += value[2]
		ate += 1

		if now_size <= ate :
			now_size +=1
			ate = 0



