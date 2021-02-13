from itertools import permutations
def solution(n, weak, dist) :
	num = len(weak)
	for i in range(len(weak)) :
		weak.append(weak[i]+n)
	
	for i in range(1,len(dist)+1) :
		for friends in list(permutations(dist, i)) :
			print('friends', friends)
			for start in range(len(weak)) :
				count = 0
				next = start
				print('start' , start)
				for friend in friends :
					while next < len(weak)-1 and weak[start] + friend >= weak[next] :
						print(weak[start], friend, weak[next])
						count += 1
						next += 1
						if count == num :
							return i
					start = next
	return -1

print(solution(12,[1, 3, 4, 9, 10],[3, 5, 7]))

def solution(n, weak, dist) :
	length = len(weak)
	for i in range(length) :
		weak.append(n+weak[i])
	
	answer = len(dist) + 1
	for start in range(length) :
		for friends in list(permutations(dist, len(dist))) :
			count = 1
			position = weak[start] + friends[count-1]
			for index in range(start, start+length) :
				if position < weak[index] :
					count += 1
					if count > len(dist) :
						break
					position = weak[index] + friends[count-1]
			answer = min(answer, count)
	if answer > len(dist) :
		return -1
	return answer

					