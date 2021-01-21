import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * 1000001
count = 1
i = 0
dp[1] = 1

while count < n :
	i += 1
	if i % 2 == 0 or i % 3 == 0 or i % 5 ==0 :
		if dp[i//2] == 1 or dp[i//3] == 0 or dp[i//5] == 0:
			count += 1
			dp[i] += 1

print(i)