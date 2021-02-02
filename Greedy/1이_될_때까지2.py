
'''
n, k = map(int, input().split())
result = 0

while True :
	target = (n//k) * k
	result += (n-target)
	n = target
	if n < k :
		break
	n //= k
	result += 1

result += (n-1)
print(result)
'''

n, k = map(int, input().split())
count = 0

while n > k :
	if n % k == 0 :
		n //= k
		count += 1
	else :
		target = n%k
		n -= target
		count += target

count += (n-1)
print(count)