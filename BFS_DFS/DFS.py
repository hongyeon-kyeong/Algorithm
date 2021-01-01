def DFS(graph, v,visited) :
	
	visited[v] = True
	print(v, end=' ')
	
	for i in graph[v] :
		if not visited[i] :
			DFS(graph, i, visited)

graph = [
	 []
	,[2,3,8]
	,[1,7]
	,[1,4,5]
	,[3,5]
	,[3,4]
	,[7]
	,[2,6,8]
	,[1,7]
]

visited = [False] * 9

DFS(graph, 1, visited)

'''
- 스택 자료구조에 기초
- 재귀함수로 풀 수 있음
- O(N)
'''