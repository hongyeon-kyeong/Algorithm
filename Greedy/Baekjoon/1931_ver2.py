n = int(input())
meetings = []
for _ in range(n) :
	start, end = map(int, input().split())
	meetings.append((start, end))

meetings.sort(key = lambda x : x[0])
meetings.sort(key = lambda x : x[1])

cur_time = 0
result = 0
for meeting in meetings :
	start, end = meeting
	if cur_time <= start :
		result += 1
		cur_time = end

print(result)