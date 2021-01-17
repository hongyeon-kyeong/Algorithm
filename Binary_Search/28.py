import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

def binary_search(array, start, end) :
	if start > end :
		return None
	
	mid = (start + end) // 2

	if array[mid] == mid  :
		return mid
	elif array[mid] > mid :
		return binary_search(array, start, mid-1)
	else :
		return binary_search(array, mid+1, end)

idx = binary_search(data, 0, n-1)
if idx == None :
	print(-1)
else :
	print(idx)


'''
5
-15 -6 1 3 7

7
-15 -4 2 8 9 13 15

7
-15 -4 3 8 9 13 15
'''