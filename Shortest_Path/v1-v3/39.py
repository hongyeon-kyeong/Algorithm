import sys
input = sys.stdin.readline
INF = int(1e9)


t = int(input())
dx = [1,-1,0,0]
dy = [0,0,-1,1]

def dijkstr(x,y, graph, energy,n) :

	for i in range(4) :
		nx = x + dx[i]
		ny = y + dy[i]

		if 0 <= nx and 0 <= ny and nx<n and ny < n :
			if energy[x][y] + graph[nx][ny] < energy[nx][ny] :
				energy[nx][ny] = energy[x][y] + graph[nx][ny]
				dijkstr(nx,ny, graph, energy, n)
		
for _ in range(t):
	n = int(input())
	graph = []
	for _ in range(n) :
		graph.append(list(map(int, input().split())))
	energy = [[INF] * (n) for _ in range(n)]
	energy[0][0] = graph[0][0]
	dijkstr(0,0, graph, energy, n)	

print(energy[n-1][n-1])

'''
1
7
9 0 5 1 1 5 3
4 1 2 1 6 5 3 
0 7 6 1 6 8 5
1 1 7 8 3 2 3
9 4 0 7 6 4 1
5 8 3 2 4 8 3
7 4 8 4 8 3 4
'''