def split_data(data) :
	num_a = 0
	num_b = 0
	for i in range(len(data)) :
		if data[i] =='(' :
			num_a += 1
		else :
			num_b += 1
		if num_a == num_b :
			return i
	return -1


def isGood(data) :
	num_a = 0
	num_b = 0

	for i in range(len(data)) :
		if data[i] =='(' :
			num_a += 1
		else :
			num_b += 1
			if num_a < num_b :
				return False
	return True

def get_u(data) :
	data = data[1:-1]
	strd = list(data)
	for i in range(len(strd)) :
		if strd[i] == '(' :
			strd[i] = ')'
		else :
			strd[i] = '('
	return ''.join(strd)

def solution(data) :
	if isGood(data) :
		#print('여기?')
		return data
	if data == '' :
		return ''

	u =[]
	v =[]
	k = split_data(data)
	u = data[0:k+1]
	v = data[k+1:]
	#print(u)
	#print(v)

	if isGood(u) :
		#print('여기')
		return u + solution(v)
	else :
		#print('저기')
		return '(' + solution(v) + ')' + get_u(u)

print(solution("()))((()"))


