import sys
from collections import deque

input = sys.stdin.readline

n, l, r = map(int, input().split())
graph = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]
count = 0

for _ in range(n) :
	graph.append(list(map(int, input().split())))

def get_union(union) :
	num = len(union)
	sum = 0
	for x, y, p in union :
		sum += p

	new_pop = (sum // num)

	for x, y, p in union :
		graph[x][y] = new_pop

def bfs(x, y, pops, visited) :
	union = []
	q = deque()
	q.append((x, y, pops))

	while q :
		#print(q.popleft())
		x, y, pops = q.popleft()
		visited[x][y] = True
		union.append((x,y,pops))

		for i in range(4) :
			nx = x + dx[i]
			ny = y + dy[i]
			
			if 0 <= nx and 0 <= ny and nx < n and ny < n :
				if l <= abs(pops - graph[nx][ny]) <= r and not visited[nx][ny]:
					q.append((nx,ny, graph[nx][ny]))
					visited[nx][ny] = True
	return union

while True :
	visited = [[False] * n for _ in range(n)]
	index = 0
	for i in range(n) :
		for j in range(n) :
			if not visited[i][j] : 
				union = bfs(i, j, graph[i][j], visited)
				index += 1
				get_union(union)
	if index == n*n :
		break
	else :
		count+=1

print(count)



