def build_stick(array_stick, array_bo, x, y) :
	if y == 0 :
		return True
	elif array_bo[x][y] == 1 or (x>0 and array_bo[x-1][y] == 1) :
		return True
	elif y > 0 and array_stick[x][y-1] == 1 :
			return True
	else :
		return False

def build_bo(array_stick, array_bo, x, y,n) :
	if (y>0 and array_stick[x][y-1] == 1) or (x<n and y>0 and array_stick[x+1][y-1]==1) :
			return True
	elif x>0 and array_bo[x-1][y] == 1 and x<n and array_bo[x+1][y] == 1 :
			return True
	else : 
		return False

def remove(array_stick, array_bo,n) :
	for i in range(n+1) :
		for j in range(n+1) :
			if array_stick[i][j]== 1 :
				if not build_stick(array_stick, array_bo, i, j) :
					return False
			if array_bo[i][j] == 1 :
				if not build_bo(array_stick, array_bo, i, j,n) :
					return False
	return True

def solution(n,build_frame) :
	array_bo = [[0]*(n+1) for _ in range(n+1)]
	array_stick = [[0]*(n+1) for _ in range(n+1)]
	
	for x, y, a, b in build_frame :
		if b == 0 :
			if a == 0 :
				array_stick[x][y] = 0
				if not remove(array_stick, array_bo, n) :
					array_stick[x][y] = 1
			else :
				array_bo[x][y] = 0
				if not remove(array_stick, array_bo, n) :
					array_bo[x][y] = 1
		else :
			if a == 0 :
				# 기둥 설치
				if build_stick(array_stick,array_bo, x, y) :
					array_stick[x][y] = 1
			else :
				# 보 설치
				if build_bo(array_stick, array_bo, x, y,n) :
					array_bo[x][y] = 1
	
	result = []
	for i in range(n+1) :
		for j in range(n+1) :
			if array_stick[i][j] != 0 :
				result.append([i, j, 0] )
			if array_bo[i][j] != 0 :
				result.append([i,j,1])
	result.sort()
	return result

print(solution(5,[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))

def possible(answer) :
	for x, y, stuff in answer :
		if stuff == 0 :
			if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer :
				continue
			return False
		elif stuff == 1 :
			if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer) :
				continue
			return False

def solution(n, build_frame) :
	answer = []
	for frame in build_frame :
		x, y, stuff, operate = frame
		if operate == 0 :
			answer.remove([x, y, stuff])
			if not possible(answer) :
				answer.append([x, y, stuff])
		if operate == 1 :
			answer.append([x, y, stuff])
			if not possible(answer) :
				answer.remove([x, y, stuff])
	return sorted(answer)