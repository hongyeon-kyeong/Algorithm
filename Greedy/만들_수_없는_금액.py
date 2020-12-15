'''
IDEA 
- 1이 없는 경우  - 1
- 1이 있는 경우 2부터 배열에서 해당수부터 작거나 같은 수를 뺀다(0이 될 때까지)

INPUT & OUTPUT
5
3 2 1 1 9
'''
N = int(input())
data = list(map(int, input().split()))

if 1 not in data :
	print(1)
else :
	res = 2
	while True :
		i = res
		print('res', res)
		for j in data :
			print('j', j)
			if j <= i :
				i -= j
			print('i', i)
			if i == 0 :
				break
		if i != 0 :
			break
		else :
			res += 1
print(res)