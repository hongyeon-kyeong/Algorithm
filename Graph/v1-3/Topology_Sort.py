from collections import deque
import sys
input = sys.stdin.readline

# 노드와 간선의 개수 입력받기
v, e = map(int, input().split())

# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (v+1)

# 각 노드에 연결된 간선 정보를 담기 위한 연결리스트(그래프) 초기화
graph = [[] for _ in range(v+1)]

# 방향그래프의 모든 간선 정보를 입력받기
for _ in range(e) :
	a, b = map(int, input().split())
	graph[a].append(b)
	indegree[b] += 1

# 위상 정렬 함수
def topology_sort() :
	q = deque()
	result = []

	for i in range(1, v+1) :
		if indegree[i] == 0 :
			q.append(i)

	# 큐가 빌 때까지 반복	
	while q  :
		idx = q.popleft()
		result.append(idx)

		for i in graph[idx] :
			indegree[i] -= 1
			if indegree[i] == 0 :
				q.append(i)

	# 위상 정렬을 수행한 결과 출력
	for i in result :
		print(i, end= ' ')

topology_sort()

'''
7 8
1 2
1 5
2 3
2 6
3 4
4 7
5 6
6 4
'''