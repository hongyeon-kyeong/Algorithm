from collections import deque

n, m = map(int, input().split())
graph = []
for _ in range(n) :
	graph.append(list(map(int, input().split())))

new_graph = [[0]*m for _ in range(n)]
for i in range(n) :
	for j in range(m) :
		new_graph[i][j] = graph[i][j]

dx = [-1,0,1,0]
dy = [0,-1,0,1]

def bfs(graph, a, b) :
	queue = deque()
	queue.append((a,b))	
	while queue :
		x, y = queue.popleft()
		
		for i in range(4) :
			nx = x + dx[i]
			ny = y + dy[i]

			if nx >= 0 and ny >= 0 and nx < n and ny < m :
				if graph[nx][ny] == 0 :
					graph[nx][ny] = 2
					queue.append((nx, ny))
	
	#print('new_graph')
	#for i in range(n) :
	#	for j in range(m) :
	#		print(graph[i][j], end=' ')
	#	print()
	#return graph

def chk_safe(graph) :
	count = 0
	for i in range(n) :
		for j in range(m) :
			if graph[i][j] == 0 :
				count += 1
	return count

answer = 0

def dfs(graph, count) :
	global answer
	if count == 3 :
		for i in range(n) :
			for j in range(m) :
				if graph[i][j] == 2 :
					bfs(graph, i, j)
		answer = max(chk_safe(graph), answer)
		for i in range(n) :
			for j in range(m) :
				graph[i][j] = new_graph[i][j]
		return

	for i in range(n) :
		for j in range(m) :
			if graph[i][j] == 0 :
				graph[i][j] = 1
				count += 1
				dfs(graph, count)
				graph[i][j] = 0
				count -= 1

dfs(graph, 0)
print(answer)

'''
array=[]
for i in range(n) :
	for j in range(m) :
		if graph[i][j] == 0 :
			array.append((i,j))

from itertools import combinations

for walls in list(combinations(array, 3)) :
	for x, y in walls :
		graph[x][y] = 1
	#bfs(graph)
	for i in range(n) :
		for j in range(m) :
			if graph[i][j] == 2 :
	#			#print(i, j)
				bfs(graph, i, j)
	answer = max(chk_safe(graph), answer)
	for i in range(n) :
		for j in range(m) :
			graph[i][j] = new_graph[i][j]

print(answer)
'''
