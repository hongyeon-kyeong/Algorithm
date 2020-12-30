import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
graph = []

for i in range(n) :
	graph.append(list(map(int, sys.stdin.readline().rstrip())))

def dfs(x, y, graph) :
	if x < 0 or y < 0 or x > n-1 or y > m-1 :
		return False

	if graph[x][y] == 0 :

		graph[x][y] = 1

		dfs(x-1, y, graph)
		dfs(x+1, y, graph)
		dfs(x, y-1, graph)
		dfs(x, y+1, graph)

		return True

	return False

result = 0
for i in range(n) :
	for j in range(m) :
		if dfs(i, j) == True :
			result += 1 

print(result)