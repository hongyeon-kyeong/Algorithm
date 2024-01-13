import sys
from collections import deque
import copy

input = sys.stdin.readline

N = int(input())
time = [0] * (1+N)
indegree = [0] * (1+N)
graph = [[] for _ in range(N+1)]

for i in range(1,N+1) :
	data = list(map(int, input().split()))
	time[i] = data[0]
	for j in range(1, len(data)-1) :
		indegree[i] += 1
		graph[data[j]].append(i)

def topology_sort() :
	result = copy.deepcopy(time)
	q = deque()
	for i in range(1, N+1) :
		if indegree[i] == 0 :
			q.append(i)

	while q :
		node = q.popleft()

		for idx in graph[node] :
			indegree[idx] -= 1
			result[idx] = max(result[idx], result[node] + time[idx])
			if indegree[idx] == 0 :
				q.append(idx)

	for i in range(1, N+1) :
		print(result[i])

topology_sort()


'''
5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1
'''


		