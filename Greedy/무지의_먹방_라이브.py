'''
IDEA
- k를 food_times 길이로 나눈 몫과 배열의 최솟값을 비교 - 더 작은 값 만큼 배열의 원소에서 각각 빼줌
- 0인 값제외한 배열길이 로 k-(뺀값)를 나누고 똑같이 함 언제까지 몫이 같거나 더 작을 때 까지
- 멈췄는데 나머지가 있는 경우 해당 인덱스 리턴
'''

'''
def solution(food_times, k):
	M = len(food_times)
	while True :
		N = 0
		min_value = 100000000
		for food in food_times :
			if food != 0 :
				N += 1
			min_v = min(food, min_value)
		
		mok = k // N
		rest = k%N
	
		if mok <= min_v :
			for i in range(M) :
				if food_times[i] != 0 :
					food_times[i] = food_times[i] - mok
			break
				
		else :
			for i in range(M) :
				if food_times[i] != 0 :
					food_times[i] = food_times[i] - min_v
			k -= min_v
	
	for i in range(M) :
		if food_times[i] == 0 :
			continue
		else :
			rest -= 1
		if rest == 0 :
			if i == M-1 :
				return 1
			else :
				return i+2
	return -1

def solution(food_times, k) :
	N = len(food_times)
	i = 0
	for _ in range(k) :
		while True : 
			if food_times[i] != 0 :
				food_times[i] -= 1
				print('i', i, food_times[i])
				i += 1
				break
			else :
				print('i', i, food_times[i])
				i += 1
				if i == N : i = 0
		if i == N : i = 0
	while True :
		if food_times[i+1] == 0 :
			i +=1
			if i+1 == N : i = -1
			print('i+1', i+1, food_times[i+1])
		else : 
			return i+2
	return -1

print(solution([3, 1, 2,3,7,5],23))
'''
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

print(solution([7,8,3,3,2,2,2,2,2,2,2,2],35))
