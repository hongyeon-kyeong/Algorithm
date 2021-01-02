import sys
N = int(sys.stdin.readline().rstrip())

d = [0] * (N+1)
d[1] = 1
d[2] = 3

for i in range(3,N+1) :
	d[i] = d[N-1] + d[N-2] + d[N-2]

print(d[N]%796796)