'''
IDEA 
1. 오름차순 정렬
2. 원소 하나씩 확인하며 수의 크기와 남은 원소의 수를 비교하여 남은 원소 수가 더 적으면 멈춤
3.  수의 크기 만큼의 원소를 지움. 카운트 올림

Trial and Error
1. remove(원소) -- 인덱스 아님!
2. 배열을 지우면 다음 for문에서 처리할 때 어려움 --> 인덱스 말고 배열의 원소를 가져오는 방식으로 FOR문을 돌리면 됨


Input & Output
5
2 3 1 2 2
-> 2
'''

N = int(input())
advs = list(map(int, input().split()))
advs.sort()
count = 0

guild = list()
for adv in advs :
	if adv > N :
		break
	else :
		for j in range(adv) :
			advs.remove(advs[j])
		count += 1
print(count)
