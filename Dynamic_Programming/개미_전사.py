import sys
N = int(sys.stdin.readline().rstrip())
d = list(map(int, sys.stdin.readline().rstrip().split()))


for i in range(N) :
	if i == 0 :
		continue
	if i == 1 :
		d[i] = max(d[i], d[i-1])
		continue

	d[i] = max (d[i-1],  d[i] + d[i-2])

print(d[N-1])