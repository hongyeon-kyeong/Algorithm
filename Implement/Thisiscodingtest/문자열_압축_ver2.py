def solution(s) :
	length = len(s)
	answer = length

	for step in range(1, length//2+1) :
		prev = s[0:step]
		compressed = ''
		count = 1
		for i in range(step,length+1,step) :
			cur = s[i: i+step]

			# 이전 문자열과 현재 문자열이 다르면
			if prev != cur :
				# 문자열 생성
				compressed += str(count) + prev if count > 1 else prev
				#print(compressed)
				prev = cur
				count = 1
			# 같으면
			else :
				count += 1
				# 문자열 압축

		compressed += str(count) + prev if count > 1 else prev
		answer = min(answer, len(compressed))
	return answer

print(solution("abcabcabcabcdededededede"))