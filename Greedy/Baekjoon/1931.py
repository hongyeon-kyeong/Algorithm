n = int(input())
meeting = []

for _ in range(n) :
	start, end = map(int, input().split())
	meeting.append((start, end))

meeting.sort(key=lambda x : x[0])
meeting.sort(key=lambda x : x[1])

cur_time = 0
count = 0
for meet in meeting :
	if cur_time <= meet[0] :
		cur_time = meet[1]
		count += 1

print(count)