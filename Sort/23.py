import sys
input = sys.stdin.readline

n = int(input())
data = []
for _ in range(n) :
	nm, k, e, m = input().split()
	data.append((nm, int(k), int(e), int(m)))
data.sort(key=lambda x : x[1], reverse=True)


for i in range(1,n) :
	for j in range(i,0,-1) :
		if data[j][1] > data[j-1][1] :
			data[j], data[j-1] = data[j-1], data[j]
		elif data[j][1] == data[j-1][1] :
			if data[j][2] < data[j-1][2] :
				data[j], data[j-1] = data[j-1], data[j]
			elif data[j][2] == data[j-1][2] :
				if data[j][3] > data[j-1][3] :
					data[j], data[j-1] = data[j-1], data[j]
				elif data[j][3] == data[j-1][3] :
					k = 0
					while True :
						if k >= len(data[j][0]) :
							 data[j], data[j-1] = data[j-1], data[j]
						elif ord(data[j][0][k]) < ord(data[j-1][0][k]) :
							 data[j], data[j-1] = data[j-1], data[j]
							 k += 1
						elif ord(data[j][0][k]) == ord(data[j-1][0][k]) :
							k +=1
							continue
						else :
							break
				else :
					break
			else :
				break
		else :
			break

for i in range(n) :
	print(data[i][0])

