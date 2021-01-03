import sys
input = sys.stdin.readline
INF = int(1e9)

# n : 노드의 개수, m : 간선의 개수
n, m = map(int, input().split())

start = int(input())

#그래프 입력받기
graph = [[] for _ in range(n+1)]
for i in range(m) :
	a, b, c = map(int, input().split())
	graph[a].append((b,c))

#print('graph')
#print(graph)
#1차원 리스트 선언
distance = [INF] * (n+1)
visited = [False] * (n+1)

def get_smallest_node() :
	min = INF
	index = 0
	for i in range(1,n+1) :
		if distance[i] < min and not visited[i]:
			min = distance[i]
			index = i
	return index


def dijkstra(start) :
	distance[start] = 0
	visited[start] = True

	for i in graph[start] :
		distance[i[0]] = i[1]
	#print('start')
	#print(distance)

	for _ in range(n-1) :
		idx = get_smallest_node()
		visited[idx] = True
		#print('idx : ', idx)

		for i in graph[idx] :
			cost = i[1] + distance[idx]
			if distance[i[0]] > cost :
				distance[i[0]] = cost 
		#print(distance)

dijkstra(start)

for i in range(1,n+1) :
	if distance[i] == INF :
		print('INFINITY')
	else :
		print(distance[i], end = ' ')


'''
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2
'''