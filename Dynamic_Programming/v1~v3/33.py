import sys
input = sys.stdin.readline

n = int(input())
time = []
pay = []
for _ in range(n) :
	t, p = map(int, input().split())
	time.append(t)
	pay.append(p)

def func(d) :
	if d + time[d] > n :
		pay[d] = 0
	res = 0
	for i in range(d):
		if i + time[i] <= d :
			res = max(res, func(i))
	pay[d] += res
	print(d, pay)
	return pay[d]

for i in range(n) :
	if i + time[i] > n :
		pay[i] = 0
	res = 0
	for j in range(i) :
		if j + time[j] <= i :
			res = max(res, pay[j])
	pay[i] += res
	#print(i, pay)

print(max(pay))
'''
7
3 10
5 20
1 10
1 20
2 15
4 40
2 200
45

10
1 1
1 2
1 3
1 4
1 5
1 6
1 7
1 8
1 9
1 10
55


'''