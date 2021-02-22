from collections import deque

n, m, k , x = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m) :
	a, b = map(int,input().split())
	graph[a].append(b)
visited = [-1] * (n+1)

def bfs(graph, start, visited) :
	queue = deque([start])
	visited[start] = 0 

	while queue :
		v = queue.popleft()
		for i in graph[v] :
			if visited[i] == -1 :
				queue.append(i)
				visited[i] = visited[v] + 1

bfs(graph, x, visited)
count = 0
for i in range(n+1) :
	if visited[i] == k :
		print(i)
		count += 1

if count == 0 :
	print -1
