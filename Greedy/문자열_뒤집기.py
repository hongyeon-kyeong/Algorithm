'''
IDEA
- 1인 덩어리와 0인 덩어리를 세서
- 더 적은 덩어리를 리턴한다

S = input()
countA = 0
countB = 0
for i in range(len(S)) :
	if i == (len(S)-1) :
		if S[i] == '0' :
			countA += 1
		else :
			countB += 1
	else :
		if S[i] != S[i+1] :
			if S[i] == '0' :
				countA += 1
			else :
				countB += 1

if countA == 0 and countB == 0 :
	print(0)
elif countA == 0 :
	print(countB)
elif countB == 0 :
	print(countA)
else :
	print(min(countA, countB))
-- 0000000인 경우를 놓쳤다.

INPUT & OUTPUT
0001100
1
'''

S = input()
countA = 0
countB = 0
for i in range(len(S)) :
	if i == (len(S)-1) :
		if S[i] == '0' :
			countA += 1
		else :
			countB += 1
	else :
		if S[i] != S[i+1] :
			if S[i] == '0' :
				countA += 1
			else :
				countB += 1

if countA + countB == 1 :
	print(0)
elif countA == 0 :
	print(countB)
elif countB == 0 :
	print(countA)
else :
	print(min(countA, countB))