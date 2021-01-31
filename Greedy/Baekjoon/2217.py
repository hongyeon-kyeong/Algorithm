import heapq
n = int(input())
ropes = []

for _ in range(n) :
	heapq.heappush(ropes,int(input()))

result = 0
while ropes :
	rope = heapq.heappop(ropes)
	result = max(result, rope*(len(ropes)+1))

print(result)