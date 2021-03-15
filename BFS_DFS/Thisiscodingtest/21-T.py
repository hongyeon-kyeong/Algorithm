from collections import deque
n, l, r = map(int, input().split())
graph = []
for _ in range(n) :
	graph.append(list(map(int, input().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def process(x, y, index) :
	united = []
	united.append((x, y))
	queue = deque()
	queue.append((x,y))
	unions[x][y] = index
	summary = graph[x][y]
	count = 1
	while queue :
		x, y = queue.popleft()
		for i in range(4) :
			nx = x + dx[i]
			ny = y + dy[i]

			if nx >= 0 and ny >= 0 and nx < n and ny < n :
				if unions[nx][ny] == -1 :
					if l <= abs(graph[nx][ny] - graph[x][y]) <= r :
						queue.append((nx, ny))
						unions[nx][ny] = index
						summary += graph[nx][ny]
						count += 1
						united.append((nx, ny))
	for a, b in united :
		graph[a][b] = summary // count

total_count = 0

while True :
	unions = [[-1] * n for _ in range(n)]
	index = 0
	for i in range(n) :
		for j in range(n) :
			if unions[i][j] == -1 :
				process(i, j, index)
				index += 1
	if index == n*n :
		break
	total_count += 1
print(total_count)