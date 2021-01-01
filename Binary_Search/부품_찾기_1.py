import sys
N = int(sys.stdin.readline().rstrip())
item = list(map(int, sys.stdin.readline().rstrip().split()))
M = int(sys.stdin.readline().rstrip())
buy = list(map(int, sys.stdin.readline().rstrip().split()))

def binary_search(array, target, start, end) :
	if start > end :
		return 'no'
	mid = (start + end) // 2
	if array[mid] == target :
		return 'yes'
	elif array[mid] > target :
		return binary_search(array, target, start, mid-1)
	else :
		return binary_search(array, target, mid+1, end)

item.sort()

for i in range(M) :
	print(binary_search(item,buy[i],0,N-1), end=' ')