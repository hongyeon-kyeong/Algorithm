'''
IDEA
- k를 food_times 길이로 나눈 몫과 배열의 최솟값을 비교 - 더 작은 값 만큼 배열의 원소에서 각각 빼줌
- 0인 값제외한 배열길이 로 k-(뺀값)를 나누고 똑같이 함 언제까지 몫이 같거나 더 작을 때 까지
- 멈췄는데 나머지가 있는 경우 해당 인덱스 리턴
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

print(solution([3, 1, 2],5))