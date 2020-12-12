

build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
n = 5
cnt = len(build_frame)

maps = [[2 for _ in range(n+1)] for _ in range(n+1)]

def build_stick(x,y) :
	if y == 0 :     # 바닥에 있거나
		return True
	if maps[x][y-1] == 0 : # 다른 기둥 위에 있거나 
			return True
	if x-1 >= 0 :
		if maps[x-1][y] == 1 :  # 보의 한쪽 끝 부분에 있거나 
			return True
	if maps[x][y] == 1 :				# 보의 한쪽 끝 부분에 있거나 
		return True
	return False

	
def build_bo(x,y) :
	#보의 한쪽 끝 부분이 기둥 위에 있거나
	if maps[x][y-1] == 0 :
			return True
	if maps[x+1][y-1] == 0 :
			return True
	# 양쪽 끝부분이 다른 보와 동시에 연결되어 있는 경우
	if x-1 >=0 and x+1 <= n :
		if maps[x-1][y] == 1 and maps[x+1][y] == 1 :
			return True
	return False

def remove(x, y) :
	for i in range(n+1) :
		for j in range(n+1) :
			if maps[i][j] == 0 :
				if build_stick(i, j) == False:
					return False
			elif maps[i][j] == 1 :
				if build_bo(i,j) == False :
					return False
	return True

for x, y, a, b in build_frame :
	if b == 1 : 
		if a == 0 :
			if build_stick(x,y) :
				maps[x][y] = 0
		else : 
			if build_bo(x,y) :
				maps[x][y] = 1
	else :
		temp = maps[x][y]
		maps[x][y] = 2
		if remove(x,y) == False :
			maps[x][y] = temp

answer = list()
for i in range(n+1) :
	for j in range(n+1)	:
		res = list()
		if maps[i][j] == 0 or maps[i][j] == 1 :
			res.append(i)
			res.append(j)
			res.append(maps[i][j])
			answer.append(res)

print(answer)

