from collections import deque
def bfs(x, y, k) :
	queue = deque()
	queue.append((x,y))
	visited[x][y] = 1

	dx = [-1,1,0,0]
	dy = [0,0,-1,1]
	while queue :
		x, y = queue.popleft()
		for i in range(4) :
			nx = x + dx[i]
			ny = y + dy[i]

			if nx >= 0 and ny >= 0 and nx < n and ny < n :
				if graph[nx][ny] > k and visited[nx][ny] == 0 :
					visited[nx][ny] = 1
					queue.append((nx, ny))

n = int(input())
graph = []
max_value = 0
for _ in range(n) :
	data = list(map(int,input().split()))
	max_value = max(max_value, max(data))
	graph.append(data)

k = 0
answer = 0
while k < max_value :
	count = 0
	visited = [[0] * n for _ in range(n)]
	for i in range(n) :
		for j in range(n) :
			if graph[i][j] > k and visited[i][j] == 0:
				bfs(i, j, k)
				count += 1
	answer = max(count, answer) 
	k += 1
print(answer)

