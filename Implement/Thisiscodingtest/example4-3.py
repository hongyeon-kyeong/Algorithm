s = input()
dx = [-1,1,-1,1,-2,-2,2,2]
dy = [-2,-2,2,2,-1,1,-1,1]

x = ord(s[0])-96
y = int(s[1])

count = 0
for i in range(8) :
	nx = x + dx[i]
	ny = y + dy[i]

	if nx < 1 or ny < 1 or nx > 8 or ny > 8 :
		continue
	else :
		count +=1
	
print(count)