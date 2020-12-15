'''
IDEA 
- 배열 번호 조합
- 두 원소가 같은 것은 제외한 후 숫자 셈

INPUT & OUTPUT
8 5
1 5 4 3 2 4 5 2
25

5 3
1 3 2 3 2
8
'''

N, M = map(int, input().split())
balls = list(map(int, input().split()))

from itertools import combinations
res = list(combinations(balls, 2))

count = 0
for r in res :
	if r[0] != r[1] :
		count += 1

print(count)