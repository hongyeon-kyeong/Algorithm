import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

data.sort()
length = len(data)
#print(data)

mid = n//2
answer1 = int(1e9)
answer2 = int(1e9)

while True :

	if mid == -1 :
		mid1 = mid + 1
		break
	sum = 0 
	#print("mid : ",mid)

	for d in data:
		v = abs(data[mid]-d)
		sum += v
	#print("sum : ",sum)

	if sum <= answer1 :
		answer1 = sum
		mid -= 1
	else : 
		mid1 = mid+1
		break

mid = n//2

while True :

	if mid == n : 
		mid2 = mid - 1
		break
	sum = 0 
	#print("mid : ",mid)

	for d in data:
		v = abs(data[mid]-d)
		sum += v
	#print("sum : ",sum)

	if sum <= answer2 :
		answer2 = sum
		mid += 1
	else : 
		mid2 = mid-1
		break

if answer1 <= answer2 :
	print(data[mid1])
else :
	print(data[mid2])


