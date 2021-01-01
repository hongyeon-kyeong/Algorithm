import sys
N, M = map(int, sys.stdin.readline().rstrip().split())
array = list(map(int, sys.stdin.readline().rstrip().split()))
start = 0
end = max(array)

result = 0
while start <= end :
	mid = (start+end) // 2

	sum = 0
	for i in range(N) :
		if array[i] > mid :
			sum += (array[i] - mid)

	if sum < M :
		end = mid-1
	else : 
		result = mid
		start = mid + 1

print(result)
