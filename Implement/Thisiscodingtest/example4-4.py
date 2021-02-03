n, m = map(int, input().split())
a, b, d = map(int, input().split())
data = [[0]*m for _ in range(n)]
array = []
for _ in range(n) :
	array.append(list(map(int, input().split())))

dx = [-1,0,1,0]
dy = [0,1,0,-1]
data[a][b] = 1

def rotate(d) :
	d -= 1
	if d == -1 :
		d == 3
		
count = 0
def move(a, b) :
	
	global count
	for _ in range(4) :
		na = a + dx[d]
		nb = b + dy[d]
		print(na,nb)

		if na < 0 or nb < 0 or na >= n or nb >= m :
			return
		
		if array[na][nb] == 0 :
			array[na][nb] = 2
			count += 1
			return move(na, nb)
		else :
			rotate(d)
	
	na = a + dx[d]*-1
	nb = b + dy[d]*-1

	if na < 0 or nb < 0 or na >= n or nb >= m :
		return

	if array[na][nb] == -1 :
		return
	else :
		return move(na,nb)

move(a,b)
print(count)

