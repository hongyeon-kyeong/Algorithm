n = int(input())
graph = []
tmp_graph = []
for _ in range(n) :
	graph.append(list(input().split()))

for i in range(n) :
	tmp_graph.append(graph[i])

def detect(a, b) :
	da = [-1,1,0,0]
	db = [0,0,-1,1]

	for d in range(4) :
		na = a + da[d]
		nb = b + db[d]

		while True :
			if na >= 0 and nb >= 0 and na < n and nb < n :
				if tmp_graph[na][nb] != 'O' :
					if tmp_graph[na][nb] == 'S' :
						return True
					else :
						na += da[d]
						nb += db[d]
				else :
					break
			else :
				break
	return False

chk = False
def dfs(count) :
	global chk
	if count == 3 :
		detect_yn = False
		for i in range(n) :
			for j in range(n) :
				if tmp_graph[i][j] == 'T' :
					if detect(i, j) :
						detect_yn = True
		if not detect_yn :
			chk = True
	else :
		for i in range(n) :
			for j in range(n) :
				if tmp_graph[i][j] == 'X' :
					count += 1
					tmp_graph[i][j] = 'O'
					dfs(count)
					count -= 1
					tmp_graph[i][j] = 'X'
dfs(0)
if chk :
	print('YES')
else :
	print('NO')
