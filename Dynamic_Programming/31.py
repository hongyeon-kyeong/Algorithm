import sys
input = sys.stdin.readline

t = int(input())

def find_gold(x, y, array, gold) :
	dx = [1,-1,0]
	dy = [1,1,1]
	
	for i in range(3) :
		nx = x + dx[i]
		ny = y + dy[i]

		if 0 <= nx and 0 <= ny and nx < n and ny < m :
			gold[nx][ny] = max(gold[x][y] + array[nx][ny], gold[nx][ny])
			find_gold(nx, ny, array, gold)


def sol(n, m, data) :
	array = [[0 for _ in range(m)] for _ in range(n)]
	gold = [[0 for _ in range(m)] for _ in range(n)]
	count = 0
	for i in range(n) :
		for j in range(m) :
			array[i][j] = data[count]
			gold[i][j] = data[count]
			count += 1
		
	for i in range(n) :
		find_gold(i,0,array,gold)
		print(gold)

	res = 0
	for i in range(n) :
		res = max(res, gold[i][m-1])

	return res

for _ in range(t) :
	n, m = map(int, input().split())
	data = list(map(int, input().split()))
	print(sol(n, m, data))


'''
2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2
'''