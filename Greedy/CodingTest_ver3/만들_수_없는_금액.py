n = int(input())
data = list(map(int, input().split()))

data.sort()
target = 1

for d in data :
	if target < d :
		break
	else :
		target += d
	
print(target)

'''
target보다 작거나 같은 동전이 주어지면 target에 동전크기만큼 더해 target을 늘릴 수 있지만, 큰 동전이 주어지면 target을 만들 방법이 없다.


'''