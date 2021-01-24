from collections import deque

v, e = map(int, input().split())
graph = [[] for _ in range(v+1)]
degree = [0] * (v+1)

for _ in range(e) :
	a, b = map(int, input().split())
	graph[a].append(b)
	degree[b] += 1

def topology_sort() :
	q = deque()
	result = []

	for i in range(1, v+1) :
		if degree[i] == 0 :
			q.append(i)

	while q :
		now = q.popleft()
		result.append(now)

		for node in graph[now] :
			degree[node] -= 1
			if degree[i] == 0 :
				q.append(i)

	for i in result :
		print(i, end=' ')
	
	topology_sort()