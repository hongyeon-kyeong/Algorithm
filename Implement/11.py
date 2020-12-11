

build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
n = 5
build_frame.sort()
print(build_frame)
cnt = len(build_frame)

maps = [[2 for _ in range(n+1)] for _ in range(n+1)]

def build_stick(x,y) :
	if x == 0 or y == 0 :     # 바닥에 있거나
		return True
	if y-1 >= 0 :
		if maps[x][y-1] == 0 : # 다른 기둥 위에 있거나 
			return True
	if x-1 >= 0 :
		if maps[x-1][y] == 1 :  # 보의 한쪽 끝 부분에 있거나 
			return True
	if maps[x][y] == 1 :				# 보의 한쪽 끝 부분에 있거나 
		return True
	return False

def remove_stick(x,y) :
	maps[x][y] = 2
	print(x,y)
	# 위에 기둥이 있을 때
	if y+1 <= n :
		if maps[x][y+1] == 0 :
			maps[x][y] = 0
	if y+1 <= n  :
		if maps[x][y+1] == 1 :
			if x+1 <= n :
				if maps[x+1][y] != 0 and maps[x+1][y+1] != 1 :
					maps[x][y] = 0
	if y+1 <= n and x-1 >= 0 :
		if maps[x-1][y+1] == 1 :
			if x-2 >=0 :
				if maps[x-1][y] != 0 and maps[x-2][y+1] != 1 :
					maps[x][y] = 0

	# 한쪽 끝만 걸친 보가 있을 때(보가 연속해서 있거나)

	
def build_bo(x,y) :
	#보의 한쪽 끝 부분이 기둥 위에 있거나
	if y-1 >=0 :
		if maps[x][y-1] == 0 :
			return True
	if x+1 <= n and y-1 >=0 :
		if maps[x+1][y-1] == 0 :
			return True
	# 양쪽 끝부분이 다른 보와 동시에 연결되어 있는 경우
	if x-1 >=0 and x+1 <= n :
		if maps[x-1][y] == 1 and maps[x+1][y] == 1 :
			return True
	return False
	
def remove_bo(x,y) :
	maps[x][y] = 2
	print(x,y)
	if x-1 >= 0 and y-1 >= 0 : 
		if maps[x-1][y] == 1 and maps[x][y-1] != 0 :
			maps[x][y] = 1
	if x+1 <= n and y-1 >= 0 :
		if maps[x+1][y] == 1 and maps[x+1][y-1] != 0 :
			maps[x][y] = 1

def remove(x, y) :
	for i in range(n+1) :
		for j in range(n+1) :
			if maps[x][y] == 0 :
				if build_stick(x, y) == False:
					return False
			elif maps[x][y] == 1 :
				if build_bo(x,y) == False :
					return False
	return True

command = list()
for i in range(cnt) :
	command = build_frame[i]

	x = command[0]
	y = command[1]
	a = command[2]
	b = command[3]

	if b == 1 : 
		if a == 0 :
			if build_stick(x,y) :
				maps[x][y] = 0
		else : 
			if build_bo(x,y) :
				maps[x][y] = 1
	else :
		if remove(x,y) :
			maps[x][y] = 2


print(maps)
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

