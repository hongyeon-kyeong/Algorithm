from collections import deque
n, l, r = map(int, input().split())
pops = []
countries =[[0] * n for _ in range(n)]
for _ in range(n) :
	pops.append(list(map(int, input().split())))

count = 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]
queue = deque()
num = 0

while True :
	for i in range(n) :
		for j in range(n) :
			if countries[i][j] == 0 :
				num += 1
				countries[i][j] = num
			queue.append((i , j))
			while queue :
				x , y = queue.popleft()
				for d in range(4) :
					nx = x + dx[d]
					ny = y + dy[d]
					if nx >= 0 and ny >= 0 and nx < n and ny < n :
						if countries[nx][ny] == 0 :
							diff = abs(pops[x][y] - pops[nx][ny]) 
							if diff <= r and diff >= l :
								queue.append((nx, ny))
								countries[nx][ny] = num
		for i in range(n) :
			for j in range(n) :
				

	if len(queue) == 0 :
		break
	else :
		count += 1
		while queue :
			country = queue.pop()ddddd
