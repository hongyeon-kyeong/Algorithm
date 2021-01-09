from collections import deque

# 도시의 개수, 도로의 개수, 거리 정보, 출발 도시 번호
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]

# 모든 도로 정보 입력받기
for _ in range(m) :
	a, b = map(int, input().split())
	graph[a].append(b)

# 모든 도시에 대한 최단 거리 초기화
distance = [-1] * (n+1)
distance[x] = 0

# 너비 우선 탐색(BFS) 수행
q = deque([x])
while q :
	now = q.popleft()
	for next_node in graph[now] :
		if distance[next_node] == -1 :
			q.append(next_node)
			distance[next_node] = distance[now] + 1

# 최단 거리가 K인 모든 도시의 번호를 오름차순으로 출력
check = False
for i in range(1, n+1) :
	if distance[i] == k :
		print(i)
		check = True

# 만약 최단거리가 K인 도시가 없다면, -1출력
if check == False :
	print(-1)