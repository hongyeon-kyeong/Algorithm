s = input()
answer = [-1]*26
for i in range(len(s)) :
	index = ord(s[i]) - ord('a')
	if answer[index] == -1 :
		answer[index] = i
print(' '.join(map(str, answer)))