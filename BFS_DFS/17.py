import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
graph = []

for _ in range(n) :
	graph.append(list(map(int, input().split())))

s, x, y = map(int, input().split())
virus = []
queue = deque()

for i in range(n) :
	for j in range(n) :
		if graph[i][j] != 0 :
			virus.append((graph[i][j],i,j,0))

dx = [1,-1,0,0]
dy = [0,0,-1,1]

virus.sort()
queue = deque(virus)
prev_time = -1

while queue :
	v = queue.popleft()
	#print(v)
	if v[3] == s :
		break
	if prev_time != v[3] :
		prev_time += 1
	for i in range(4) :
		nx = v[1] + dx[i]
		ny = v[2] + dy[i]

		if nx >= 0 and ny >= 0 and nx < n and ny < n :
			if graph[nx][ny] == 0 :
				queue.append((v[0], nx, ny, prev_time+1))
				graph[nx][ny] = v[0]

print(graph[x-1][y-1])