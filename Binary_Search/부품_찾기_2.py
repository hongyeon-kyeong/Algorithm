import sys
N = int(sys.stdin.readline().rstrip())
count = [0] * 1000001

for i in sys.stdin.readline().rstrip().split() :
	count[int(i)] += 1

M = int(sys.stdin.readline().rstrip())
buy = list(map(int, sys.stdin.readline().rstrip().split()))

for i in buy :
	if count[i] == 1 :
		print('yes', end=' ')
	else :
		print('no', end=' ')