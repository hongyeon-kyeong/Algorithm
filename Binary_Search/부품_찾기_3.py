import sys
N = sys.stdin.readline().rstrip()
array = set(map(int, sys.stdin.readline().rstrip().split()))

M = sys.stdin.readline().rstrip()
x = list(map(int, sys.stdin.readline().rstrip().split()))

for i in x :
	if i in array :
		print('yes', end=' ')
	else :
		print('no', end= ' ')