import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수
N = int(input())
# 간선의 개수
M = int(input())

# 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
graph = [[INF for _ in range(N+1)] for _ in range(N+1)]

# 간선 정보
for _ in range(M) :
	a, b, c = map(int, input().split())
	graph[a][b] = c

# 자기 자신은 0으로 초기화
for i in range(1,N+1) :
	graph[i][i] = 0

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for i in range(1,N+1) :
	for j in range(1, N+1) :
		for k in range(1,N+1) :
			graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])

# 수행된 결과를 출력
for i in range(1, N+1) :
	for j in range(1, N+1) :
		if graph[i][j] == INF :
			print('INFINITY')
		else :
			print(graph[i][j], end =' ')
	print()

'''
4
7
1 2 4
1 4 6
2 1 3
2 3 7
3 1 5
3 4 4
4 3 2
'''