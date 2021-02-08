def solution(s) :
	length = len(s)
	result = length

	# 0 부터 length-1까지 
	for i in range(1,length+1) :
		# i 만큼 슬라이싱
		count = 1
		new_string = ''
		zip_string = s[0:i]
		for j in range(0,length-i,i) :
			str_1 = s[j:j+i]
			str_2 = s[j+i:j+i*2]
			#print('str_1, str_2 :', str_1, str_2)

			if str_1 == str_2 :
				count += 1
				zip_string = str(count) + str_1
				#print('equal : ', zip_string )
			else :
				count = 1
				new_string += zip_string
				zip_string = str_2
				#print('diff : ' , new_string)
		
		new_string += zip_string
		#print('fin >>>>>>>>>> ' , new_string)
		result = min(len(new_string), result)
	return result

def solution2(s) :
	answer = len(s)

	for step in range(1, len(s)//2 + 1) :
		count = 1
		compressed = ''
		prev = s[0:step]
		for j in range(step, len(s), step) :
			if prev == s[j:j+step] :
				count += 1
			else :
				compressed += str(count) + prev if count >=2 else prev
				prev = s[j:j+step]
				count = 1
		compressed = str(count) + prev if count >=2 else prev
		answer = min(answer, len(compressed))
	return answer



print(solution("xababcdcdababcdcd"))


