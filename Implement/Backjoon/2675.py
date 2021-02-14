n = int(input())
for _ in range(n) :
	r, s = input().split()
	for ss in s :
		print(ss*int(r), end='')
	print()