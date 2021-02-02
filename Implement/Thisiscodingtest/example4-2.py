n = int(input())
count = 0

hour = 0 
mins = 0
seconds = 0

while hour <= n :
	seconds += 1
	if seconds > 59 :
		mins += 1
		seconds = 0
	if mins > 59 :
		hour += 1
		mins = 0
		seconds = 0
	
	if '3' in str(hour) or '3' in str(mins) or '3' in str(seconds) :
		count += 1

print(count)

for i in range(n+1) :
	for j in range(60) :
		for k in range(60) :
			if '3' in str(i) + str(j) + str(k) :
				count+=1

# 최대 24 * 60 * 60 으로 100만 건 이하의 연산횟수이기 때문에 완전탐색이 가능하다.