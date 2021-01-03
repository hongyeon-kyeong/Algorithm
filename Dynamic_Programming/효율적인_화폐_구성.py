import sys
N, M = map(int, sys.stdin.readline().rstrip().split())

coin = []
for _ in range(N) :
	coin.append(int(sys.stdin.readline().rstrip()))

d = [0] * 10001
for i in range(1,M+1) :
	min = 10001
	for j in range(N) :
		if i - coin[j] >= 0 :
			if min > d[i - coin[j]] :
				min = d[i-coin[j]]
	if min < 10001 :
		d[i] = min + 1
	else :
		d[i] = 10001

if d[M] == 10001 :
	print(-1)
else :
	print(d[M])	
