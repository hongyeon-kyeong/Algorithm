from collections import deque
import sys
INF = int(1e9)

def bfs(graph, start, visited) :
	queue = deque([start])
	visited[start] = 0
	
	while queue :
		v = queue.popleft()

		for i in graph[v] :
			if visited[i] == INF :
				queue.append(i)
				visited[i] = visited[v] + 1

input = sys.stdin.readline
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m) :
	a, b = map(int, input().split())
	graph[a].append(b)
visited = [INF] * (n+1)

bfs(graph, x, visited)
count = 0

for i in range(1,n+1) :
	if visited[i] == k :
		count+=1
		print(i)

if count == 0 :
	print(-1)