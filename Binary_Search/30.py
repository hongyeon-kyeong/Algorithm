def get_wildcard(string, length) :
	start = 0
	end = length - 1

	if string[0] == "?" :
		while start <= end :
			mid = (start + end) // 2
			if (mid == length-1 or string[mid+1] != "?") and string[mid] == "?" :
				return ("f", mid)
			elif string[mid] == "?" and string[mid+1] == "?":
				start = mid + 1
			else :	
				end = mid - 1
	else :
		while start <= end :
			mid = (start + end) // 2
			if (string[mid-1] != "?" or mid == 0) and string[mid] == "?" :
				return ("e", mid)
			elif string[mid] == "?" and string[mid-1] == "?" :
				end = mid - 1
			else :
				start = mid + 1

def solution(words, queries) :
	result = []
	for i in range(len(queries)) :
		count = 0
		n = len(queries[i])
		type, idx = get_wildcard(queries[i], n)
		#print(type, idx)

		for j in range(len(words)) :
			if n == len(words[j]) :
				flag = True
				if type == "f" :
					for k in range(idx+1,n) :
						if queries[i][k] != words[j][k] :
							flag = False
							break
					if flag :
						#print(words[j])
						count += 1
				else :
					for k in range(0,idx) :
						if queries[i][k] !=  words[j][k] :
							flag = False
							break
					if flag :
						#print(words[j])	
						count += 1

		result.append(count)
	return result


#print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],["fro??", "????o", "fr???", "fro???", "pro?"]))
print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],["?????"]))