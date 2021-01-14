def solution(n, stages) :
	count =  [0] * (n+2)
	fail = []
	length = len(stages)

	for i in stages :
		count[i] += 1
	#print(count)

	for i in range(1,n+1) :
		if length == 0 :
			fail.append((i,0))
		else :
			fail.append((i, count[i] / length))
			length -= count[i]
	#print(fail)

	fail.sort(key=lambda x : -x[1])
	#print(fail)

	result = []
	for i in range(n) :
		result.append(fail[i][0])
	
	return result

#print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4,[4,4,4,4,4]))


	