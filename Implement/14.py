
def cut_array(num, weak) :
	res = list()
	for i in range(num) :
		r = list()
		res.append(r)
	return res

def chk_len(r, dist) :
	if len(r) == 1 : return 1
	else :
		str = r[0]
		fin = r[len(r)-1]

		if str > fin : return 12-(str-fin)
		else : return fin-str

def solution(n, weak, dist) :
	m = len(dist)
	for i in range(m) : 
		answer = i
		res = cut_array(i, weak)
		len_list = list()
		for r in res :
			len_list.append(chk_len(r,dist))
		
		len_list.sort()
		dist.sort()
		for i in range(len(len_list)) :
			if dist[i] < len_list[i] :
				answer = -1
				break
		if answer != -1 :
			return answer
	return answer