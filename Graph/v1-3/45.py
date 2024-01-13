import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for _ in range(t) :
	n = int(input())
	data = list(map(int, input().split()))
	graph = [[] for _ in range(n+1)]
	indegree = [0] * (n+1)

	for i in range(n-1) :
		for j in range(i+1, n) :
			#print(data[i], data[j])
			graph[data[i]].append(data[j])
			indegree[data[j]] += 1
	#print(graph)
	m = int(input())

	for _ in range(m) :
		a, b = map(int, input().split())

		if b in graph[a] :
			graph[a].remove(b)
			graph[b].append(a)
			indegree[b] -= 1
			indegree[a] += 1
		else :
			graph[b].remove(a)
			graph[a].append(b)
			indegree[a] -= 1
			indegree[b] += 1
	
	#print(graph)
	q = deque()

	for i in range(1,n+1) :
		if indegree[i] == 0 :
			q.append(i)

	result = []
	total = 0
	status = ''
	while q :
		now = q.popleft()
		result.append(now)
		count = 0
		total += 1

		for v in graph[now] :
			indegree[v] -= 1
			if indegree[v] == 0 :
				count += 1
				q.append(v)
			
			if count > 1 :
				status ='not certain'

	if status == 'not certain' :
		print('?')
	elif total < n :
		print('IMPOSSIBLE')
	else :
		print(' '.join(map(str, result)))
