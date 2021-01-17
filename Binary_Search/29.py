n, c = map(int, input().split(' '))

array = []
for _ in range(n) :
	array.append(int(input()))
array.sort()
#print(array)

#start = array[1] - array[0]
#end = array[n-1] - array[0]
start = 1
end = array[n-1] - array[0]
result = 0

while start <= end :
	mid = (start + end) // 2
	#print(start, end, mid)
	value = array[0]
	count = 1

	for i in range(1,n) :
		if array[i] >= value + mid :
			value = array[i]
			count += 1
	if count >= c :
		start = mid + 1
		result = mid
	else :
		end = mid - 1

print(result)