#11
N = int(input())
K = int(input())

time = list()
direction = list()
maps = [[0 for _ in range(N)] for _ in range(N)]
for _ in range(K) :
  a, b = list(map(int, input().split()))
  maps[a-1][b-1] = 2
L = int(input())
for _ in range(L) :
  C, X = list(input().split())
  time.append(int(C))
  direction.append(X)

dx = [0,1,0,-1]
dy = [1,0,-1,0]
count = 0
maps[0][0] = 1
i = 0
d = 0
x=0
y=0
snake_x = list()
snake_y = list()
tail = 0
snake_x.append(x)
snake_y.append(y)

print(time)
while True :
  if count in time :
    if direction[i] == 'D':
      d += 1
    else :
      d -= 1
    i+=1
    if i==4 : i = 0
    elif i==-1 : i=3
  nx = x + dx[d]
  ny = y + dy[d]
  
  if nx == N or ny == N or nx == -1 or ny == -1 :
    break
  if maps[nx][ny] == 1 :
    break
  
  count += 1
  x = nx
  y = ny
  snake_x.append(x)
  snake_y.append(y)

  if maps[x][y] != 2 :
    maps[snake_x[tail]][snake_y[tail]] = 0
    tail += 1

  maps[x][y] = 1

print(count+1)
