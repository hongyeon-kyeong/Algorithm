def rotate(key) :
	m = len(key)
	new_key = [[0]*m for _ in range(m)]
	for i in range(m) :
		for j in range(m) :
			new_key[i][j] = key[j][(m-1-i)]
	
	return new_key

def solution(key, lock) :
	n = len(lock)
	new_lock = [[0]*3*n for _ in range(3*n)]
	# 자물쇠 크기 늘리기
	for i in range(n) :
		for j in range(n) :
			new_lock[n+i][n+j] = lock[i][j]

	# 맞춰보기
	for i in range(n*2) :
		for j in range(n*2) :
			r_count = 0
			while r_count < 4 :
				chk = True
				for a in range(len(key)) :
					for b in range(len(key)) :
						new_lock[i+a][j+b] += key[a][b]

				for a in range(n,n*2) :
					for b in range(n, n*2) :
						if new_lock[a][b] != 1 :
							chk = False
				
				if not chk :
					for a in range(len(key)) :
						for b in range(len(key)) :
							new_lock[i+a][j+b] -= key[a][b]
					key = rotate(key)
					r_count += 1
				else :
					return True
	return False
print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],[[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
