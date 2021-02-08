n = input()
idx = len(n) // 2
sum_left = 0
sum_right = 0
for i in range(idx) :
	sum_left += int(n[i])
	sum_right += int(n[len(n)-i-1])

if sum_left == sum_right :
	print('LUCKY')
else :
	print('READY')


