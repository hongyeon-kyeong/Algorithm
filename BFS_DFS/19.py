import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
data = list(map(int, input().split()))
opt = ['+','-','*','/']

def make_ops(opts, num, op) :
	while num > 0 :
		opts.append(op)
		num -= 1
	return opts

opts = []

for i in range(4) :
	make_ops(opts, data[i], opt[i])

resultx = int(-1e9)
resultm = int(1e9)

for operators in list(permutations(opts,len(opts))) :
	sum = nums[0]
	for i in range(n-1) :
		if operators[i] == '+' :
			sum += nums[i+1]
		elif operators[i] == '-' :
			sum -= nums[i+1]
		elif operators[i] == '*' :
			sum *= nums[i+1]
		else :
			if sum < 0 and nums[i+1] > 0 :
				sum *= -1
				sum //= nums[i+1]
				sum *= -1
			else :
				sum //= nums[i+1]
	resultx = max(resultx, sum)
	resultm = min(resultm, sum)

print(resultx)
print(resultm)