import sys
input = sys.stdin.readline

n = int(input())
graph = []
temp = []

for _ in range(n) :
	graph.append(list(input().split()))

temp = [[0] * n for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]


def watch(x, y, temp, k) :
	nx = x + dx[k]
	ny = y + dy[k]

	if 0 <= nx and 0 <= ny and nx < n and ny < n :
		if temp[nx][ny] == 'X' :
			return watch(nx, ny, temp, k)
		elif temp[nx][ny] == 'S' :
			return False
	return True

find = False

def dfs(count) :
	global find
	if count == 3 :
		#check = True
		for i in range(n) :
			for j in range(n) :
				temp[i][j] = graph[i][j]
		for i in range(n) :
			for j in range(n) :
				if graph[i][j] == 'T' :
					for k in range(4) :
						if watch(i, j, temp, k) == False :
							return False
		return True
	else :
		for i in range(n) :
			for j in range(n) :
				if graph[i][j] == 'X' :
					graph[i][j] = 'O'
					count += 1
					if dfs(count) :
						find = True
						return 
					graph[i][j] = 'X'
					count -= 1
dfs(0)	

if find :
	print('YES')
else :
	print('NO')