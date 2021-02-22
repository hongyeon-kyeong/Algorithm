from collections import deque

n, m = map(int, input().split())
array = []
for _ in range(n) :
	array.append(list(map(int, input())))

graph = [[0]*m for _ in range(n)]

dx = [-1,0,1,0]
dy = [0,-1,0,1]

def bfs(x, y) :
	queue = deque([(x,y)])
	graph[x][y] = 1 

	while queue :
		a, b = queue.popleft()

		for i in range(4) :
			na = a + dx[i]
			nb = b + dy[i]

			if na >= 0 and nb >= 0 and na < n and nb < m :
				if array[na][nb] == 1 and graph[na][nb] == 0 :
					queue.append((na, nb))
					graph[na][nb] = graph[a][b] + 1
bfs(0,0)
print(graph[n-1][m-1])
					


