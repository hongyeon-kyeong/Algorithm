def turn(key) :
	new_key = [[0]* len(key) for _ in range(len(key))]
	for i in range(len(key)) :
		for j in range(len(key)) :
			new_key[i][j] = key[j][len(key)-1-i]
	return new_key		
			
def solution(key, lock) :
	
	m = len(key)
	n = len(lock)
	
	result = [[0]*n for _ in range(n)]

	for a in range(-n, n+1) :
		for b in range(-n, n+1) :
			turn_time = 0
			while turn_time < 4 :
				check = True
				for i in range(n) :
					for j in range(n) :
						result[i][j] = lock[i][j]
						
				for i in range(m) :
					for j in range(m) :
						if i-a >= 0 and j-b>=0 and i-a<n and j-b<n :

							result[i-a][j-b] += key[i][j]
				
				for i in range(n) :
					for j in range(n) :
						if result[i][j] != 1 :
							check = False

				if not check :
					key = turn(key)
					turn_time += 1
				else :
					return 'true'
	return 'false'

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],[[1, 1, 1], [1, 1, 0], [1, 0, 1]]))


def rotate_a_matrix_by_90_degree(a) :
	n = len(a)
	m = len(a[0])

	result = [[0]*n for _ in range(m)]

	for i in range(n) :
		for j in range(m) :
			result[j][n-i-1] = a[i][j]
	return result

def check(new_lock) :
	lock_length = len(new_lock) // 3
	for i in range(lock_length, lock_length*2) :
		for j in range(lock_length, lock_length*2) :
			if new_lock[i][j] != 1 :
				return False
	return True

def solution(key, lock) :
	n = len(lock)
	m = len(key)

	new_lock = [[0]*(n*3) for _ in range(n*3)]

	for i in range(n) :
		for j in range(n) :
			new_lock[i+n][j+n] = lock[i][j]

	for rotation in range(4) :
		key = rotate_a_matrix_by_90_degree(key) 
		for x in range(n*2) :
			for y in range(n*2) :
				for i in range(m) :
					for j in range(m) :
						new_lock[x+i][y+j] += key[i][j]
				if check(new_lock) :
					return True
				for i in range(m)  :
					for j in range(m) :
						new_lock[x+i][y+j] -= key[i][j]
		return False
