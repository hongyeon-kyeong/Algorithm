import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

n, x = map(int, input().split())
data = list(map(int, input().split()))

right_index = bisect_right(data, x)
left_index = bisect_left(data, x)

if right_index == left_index :
	print(-1)
else :
	print(right_index-left_index)

'''
7 2
1 1 2 2 2 2 3

7 4
1 1 2 2 2 2 3
'''