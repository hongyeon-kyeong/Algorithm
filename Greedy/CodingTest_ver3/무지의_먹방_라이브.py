import heapq
def solution(food_times, k) :
	h = []

	for i in range(len(food_times)) :
		heapq.heappush(h, (food_times[i], i+1))

	sum_value = 0
	previous = 0
	length = len(food_times)
	while sum_value + (h[0][0] - previous) * length <= k :
		now = heapq.heappop(h)[0]
		sum_value += (now-previous) * length
		length -= 1
		previous = now

		if length == 0 :
			return -1

	result = sorted(h, key= lambda x : x[1])
	return result[(k-sum_value)%length][1]

print(solution([3,1,2],5))