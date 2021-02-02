S = input()
count_a = 0
count_b = 0

for i in range(len(S)) :
	if i == len(S)-1 :
		if int(S[i]) == 0 :
			count_a += 1
		else :
			count_b += 1
	else :
		if	S[i] != S[i+1] :
			if int(S[i]) == 0 :
				count_a  += 1
			else :
				count_b  += 1

print(min(count_a, count_b))
