import sys
input = sys.stdin.readline

n = int(input())
data = [[] for _ in range(n)]
for i in range(n) :
	data[i] = list(map(int, input().split()))
	for _ in range(n-i-1) :
		data[i].append(-1)

for i in range(1,n) :
	for j in range(n) :
		if j==0 :
			data[i][j] = data[i-1][j] + data[i][j]
		elif j == n-1 :
			data[i][j] = data[i-1][j-1] + data[i][j]
		else :
			data[i][j] = max(data[i-1][j-1], data[i-1][j]) + data[i][j]
res = 0
for i in range(n) :
	res = max(res, data[n-1][i])

print(res)

'''
5
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5  
'''

#print(data)