n, m = map(int, input().split())
array = []

'''
for i in range(n) :
	s = input()
	for string in s :
		array[i].append(int(string))
'''
for i in range(n) :
	array.append(list(map(int, input())))

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def dfs(array, x, y) :
	if array[x][y] == 0 :
		array[x][y] = 2

		for k in range(4) :
			nx = x + dx[k]
			ny = y + dy[k]
			if nx >=0 and ny >= 0 and nx < n  and ny < m :
				dfs(array, nx, ny)

count = 0
for i in range(n) :
	for j in range(m) :
		if array[i][j] == 0 :
			dfs(array, i, j)
			count += 1
			print(i, j, count)

print(count)
