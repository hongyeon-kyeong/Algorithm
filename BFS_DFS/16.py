from itertools import combinations
import copy

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def dfs(graph, x, y) :

	for i in range(4) :
		nx = x + dx[i]
		ny = y + dy[i]

		if nx < 0 or ny < 0 or nx >= n or ny >= m :
			continue
		if graph[nx][ny] == 0 :
			graph[nx][ny] = 2
			dfs(graph, nx, ny)

n, m = map(int, input().split())
graph = []
for _ in range(n) :
	graph.append(list(map(int, input().split())))

blank = []
for i in range(n) :
	for j in range(m) :
		if graph[i][j] == 0 :
			blank.append((i, j))

answer = 0
for walls in list(combinations(blank, 3)) :
	maps = copy.deepcopy(graph)
	count = 0
	for wall in walls :
		maps[wall[0]][wall[1]] = 1
	
	for i in range(n) :
		for j in range(m) :
			if maps[i][j] == 2 :
				dfs(maps,i, j)

	for i in range(n) :
		for j in range(m) :
			if maps[i][j] == 0 :
				count += 1

	answer = max(answer, count)

print(answer)