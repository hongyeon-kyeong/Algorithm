def split_balance(data) :
	count_a = 0
	count_b = 0
	for i in range(len(data)) :
		if data[i] == '(' :
			count_a += 1
		else :
			count_b += 1
		
		if count_a == count_b :
			return data[0:i+1], data[i+1:]

'''
count_a, count_b 2개 선언하지 않고 count 하나로 처리할 수도 있다.
def split_balance(data) ;
	count = 0
	for i in range(len(data)) :
		if data[i] == '(' :
			count += 1
		else :
			count -= 1
		if count == 0 :
			return i

def isGood(data) :
	count = 0
	for i in p :
		if i == '(' :
			count += 1
		else :
			if count == 0 : 
				return False
			count -= 1
	return True 
'''

def isGood(data) :
	count_a = 0
	count_b = 0
	for i in range(len(data)) :
		if data[i] == '(' :
			count_a += 1
		else :
			count_b += 1
		
		if count_a < count_b :
			return False
	return True

def make_newu(data) :
	data = data[1:-1]
	new_data = ''
	for i in range(len(data)) :
		if data[i] == '(' :
			new_data += ')'
		else :
			new_data += '('
	return new_data

def solution(p) :
	if p == '' :
		return ''
	
	u, v = split_balance(p)
	if isGood(u) :
		return u + solution(v)
	else :
		return '(' + solution(v) + ')' + make_newu(u)

print(solution('()))((()'))
