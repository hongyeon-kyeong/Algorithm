import sys
input = sys.stdin.readline

n = int(input())
data = []
for _ in range(n) :
	data.append(int(input()))

data.sort()

prev_sum = data[0]
answer = 0 
for i in range(1,n) :
	prev_sum += data[i]
	answer += prev_sum


print(answer)


