
n, k = map(int, input().split())
graph = []
virus = []
for i in range(n) :
	data = list(map(int, input().split()))
	graph.append(data)
	for j in range(n) :
		if data[j] != 0 :
			virus.append((data[j], i, j,0))
s, x, y = map(int, input().split())
virus.sort()

time_count = 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]


while virus :
	v, a, b, time_count = virus.pop(0)

	if time_count == s :
		print(graph[x-1][y-1])
		break

	for i in range(4) :
		na = a + dx[i]
		nb = b + dy[i]

		if na > 0 and nb > 0 and na < n and nb < n :
			if graph[na][nb] == 0 :
				virus.append((v, na, nb, time_count+1))
				graph[na][nb] = v
