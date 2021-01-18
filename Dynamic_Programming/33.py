import sys
input = sys.stdin.readline

n = int(input())
time = []
pay = []
for _ in range(n) :
	t, p = map(int, input().split())
	time.append(t)
	pay.append(t)

def func(d) :
	if d + time[d] > n :
		pay[d] = 0
	for i in range(d):
		if i + time[i] <= d :
			pay[d] = max(pay[d], func(i))
	return pay[d]

print(func(n-1))
