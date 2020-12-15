'''
IDEA
1. 피연산자가 0이 아니면 무조건 곱하기 우선으로

INPUT & OUTPUT
02984 -> 576
567 -> 210
'''

S = input()
num = list()
for s in S :
	num.append(int(s))
sum = 0
for n in num :
	if n == 0 or sum == 0 :
		sum += n 
	else :
		sum *= n
print(sum)
	