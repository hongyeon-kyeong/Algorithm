'''
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort(reverse=True)
sum = 0
count = 0
i = 0

while m > 0 :
	if count == k :
		count = 0
		sum += data[1]
	else :
		sum += data[0]
		count += 1
	m -= 1

print(sum)
'''
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort(reverse=True)
first = data[0]
second = data[1]
sum = 0
count = 0

while True :
	if m == 0 :
		break
	if count < k :
		sum += first
		count += 1
	else :
		sum += second
		count = 0
	n -= 1

print(sum)

