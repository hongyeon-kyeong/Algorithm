import sys
input = sys.stdin.readline
import heapq
INF = int(1e9)

dx = [-1,0,1,0]
dy = [0,-1,0,1]

for tc in range(int(input())) :
	n = int(input())
	graph = []
	for _ in range(n) :
		graph.append(list(map(int, input().split())))
	
	distance = [[INF] * n for _ in range(n)]

	x, y  = 0 , 0
	q = [(graph[x][y],x,y)]
	distance[x][y] = graph[x][y]

	while q :
		dist, x, y = heapq.heappop(q)

		# 현재 노드가 이미 처리된 적이 있으면?
		#if distance[x][y] < dist :
		#	continue
		
		for i in range(4) :
			nx = x + dx[i]
			ny = y + dy[i]

			if nx < 0 or ny >=n or ny < 0 or nx >= n :
				continue
			
			cost = dist + graph[nx][ny]

			if cost < distance[nx][ny] :
				distance[nx][ny] = cost
				heapq.heappush(q, (cost, nx, ny))
'''
	distance[0][0] = graph[0][0]

	h = []
	heapq.heappush(h, (distance[0][0], 0, 0))
	
	while h :
		now = heapq.heappop(h)

		for i in range(4) :
			nx = now[1] + dx[i]
			ny = now[2] + dy[i]

			if 0 <= nx and 0 <= ny and nx < n  and ny < n :
				if now[0] + graph[nx][ny] < distance[nx][ny] :
					distance[nx][ny] = now[0] +  graph[nx][ny]
					heapq.heappush(h, (distance[nx][ny], nx, ny))
'''
print(distance[n-1][n-1])