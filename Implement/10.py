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

def turn() :
	for x in range(len(key)) :
		for y in range(len(key)) :
			new_y = len(key) - 1 - x
			new_x = y

			new_key[new_x][new_y] = key[x][y]
	print('new_key : ', new_key)

lock = list()
N = len(key)
a = N-1
b = N-1
M = len(lock)
turn_count = 0
while b < (N+M) :
	while a < (N + M) :
		while turn_count <= 4 :
			for i in range(N) :
				for j in range(N) :
					if a+i < 0 or a+i > N-1  or b+j < 0 or b+j > N-1 :
						continue 
					else :
						if key[i][j] + lock[a+i][b+j] == 0 :
							break_yn = True
							break
				if break_yn == True :
					break 
		turn()
		turn_count += 1
	a+=1
b+=1




