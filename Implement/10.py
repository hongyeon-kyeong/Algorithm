def rotate(n, key) :
	new_key = [[0 for _ in range(n)] for _ in range(n)]

	for i in range(n) :
		for j in range(n) :
			x = j
			y = n-1-i
			new_key[x][y] = key[i][j]
	
	return new_key

def check_break(m, res) :
	for i in range(m) :
		for j in range(m) :
			if res[i][j] != 1 :
				return False
	return True

def create_res(key, lock, n, m, a, b) :
		res = [[0 for _ in range(m)] for _ in range(m)]
		for i in range(m) :
			for j in range(m) :
				if i+a < 0 or i+a >= n or j+b < 0 or j+b >= n :
					res[i][j] = lock[i][j]
				else :
					res[i][j] = key[i+a][j+b] + lock[i][j]
		return res

def solution(key, lock) :
	n = len(key)
	m = len(lock)
	count = 0

	for a in range(-(m-1), m) :
		for b in range(-(m-1), m) :
			for count in range(4) :
				res = create_res(key, lock,n, m, a, b)
				if check_break(m,res) :
					return True
				else :
					key = rotate(n, key)
	return False