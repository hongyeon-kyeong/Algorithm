s = input()
group_a = 0
group_b = 0 
for i in range(len(s)) :
	if i < len(s)-1 :
		if s[i+1] != s[i]:
			if s[i] == "0" :
				group_a += 1
			else :
				group_b += 1
	else :
		if s[i] == "0" :
			group_a += 1
		else :
			group_b += 1	

print(min(group_a, group_b))


