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

# 너무 작은 로프가 들어오면 오히려 최대중량이 떨어지게 됨.abs
# 새로 배열에 넣어서 최솟값을 구하는 게 아니면 굳이 힙을 쓰지 않고 배열을 사용한 후 정렬해도 된다.