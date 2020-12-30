'''
# 내 풀이
def find_food(food_times,i,n) :
	count2 = 0
	if i == n :
		i = 0
	
	while food_times[i] == 0 :
		i += 1
		count2 += 1
		#print('i', i , 'count2', count2)
		if count2 == n :
			return -2
		if i == n :
			i = 0
	return i

def solution(food_times, k) :
	food = -1
	count = 0
	n = len(food_times)
	while count < k :
		food = find_food(food_times, food+1, n)
		if food == -2 :
			return -1
		food_times[food] -= 1  # 먹었다.
		count += 1 # 1초가 지났다.
		print(count, food_times, food)
	res = find_food(food_times, food+1,n)
	return res+1
'''
import heapq

def solution(food_times, k) :

	if sum(food_times) <= k :
		return -1
	
	q = []
	for i in range(len(food_times)) :
		heapq.heappush(q,(food_times[i],i+1))

	sum_value = 0
	previous = 0
	length = len(food_times)
	while sum_value + (q[0][0]-previous) * length <= k :
		now = heapq.heappop(q)[0]
		sum_value += (now-previous) * length
		length -= 1
		previous = now

	result = sorted(q, key=lambda x : x[1])
	return result[(k-sum_value)%length][1]
print(solution([7,8,3,3,2,2,2,2,2,2,2,2],35))
