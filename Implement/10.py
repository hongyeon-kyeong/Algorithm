'''
* range test
arry = [[i for i in range(5)] for _ in range(5)]

for x in arry :
	print('x : ', x)
	#print('y : ',y)

for x, y in arry :
	print('x : ', x)
	print('y : ', y)

#ValueError: too many values to unpack (expected 2) 

* length of array : number of rows

arry = [[i for i in range(5)] for _ in range(5)]
print(len(arry))
# 5

arry = [[i for i in range(5)] for _ in range(4)]
print(len(arry))
# 4

'''

# 90 rotation func.

key = list()
for _ in range(3) :
	key.append(list(map(int, input().split())))
new_key = [[0 for _ in range(len(key))] for _ in range(len(key))]
print("key : ", key)

lock = list()
for _ in range(3) :
	lock.append(list(map(int, input().split())))


N = len(key)
a = N-1
b = N-1
M = len(lock)
count = 0


def turn(key) :
	for x in range(len(key)) :
		for y in range(len(key)) :
			print('x', x, 'y', y)
			new_y = len(key) - 1 - x
			new_x = y
			print('new_x', new_x, 'new_y', new_y, 'new_key' , key[x][y])
			new_key[new_x][new_y] = key[x][y]
	return new_key

flag = False
for a  in range(-N+1, N) :
	for b in range(-N+1, N) :
		while count < 4 :
			'''
			flag = True
			new_lock = [[0 for _ in range(len(key))] for _ in range(len(key))]
			for i in range(N) :
				for j in range(N) :
					print('왔니?', a, b, i, j)
					print('lock : ', lock)
					if lock[i][j] == 1:
						new_lock[i][j] = 1
					else :
						if i+a < 0 or j+b < 0  or i+a >= N or j+b >=N : continue
						else :
							new_lock[i][j] = key[i+a][j+b] + lock[i][j]
							print('왔다 ! ', i, j)
							print('a, b : ', a, b)
			for i in range(N) :
				for j in range(N) :
					if new_lock[i][j] != 1 :
						flag = False
						break
			if flag == True : break
			'''
			new_key = turn(key)
			key = new_key[:]
			print(key)
			count += 1
		if flag == True : break
	if flag == True : break
print(flag)


''''
print(key)
break_yn = False
turn_count = 0
while b < (N+M) :
	print('b : ', b)
	while a < (N + M) :
		print('a : ', a)
		while turn_count <= 4 :
			print('turn_count : ', turn_count)
			for i in range(N) :
				print('i : ' , i)
				for j in range(N) :
					print('j : ' , j)
					print('a + i', a+i)
					print('b + j', b+j)
					if a+i < 0 or a+i > N-1  or b+j < 0 or b+j > N-1 :
						continue 
					else :
						if key[i][j] + lock[a+i][b+j] != 1 :
							break_yn = True
							break
				if break_yn == True :
					break 
			if break_yn == False :
				print('2')
				break
		turn()
		turn_count += 1
	a+=1
b+=1
'''




