array = [5,7,9,0,3,1,6,2,4,8]
#array = [2,2,2,2,1,1,1,2,1,1]

def quick_sort(start, end, array) :
	if start >= end :
		return
	
	pivot = start
	left = start +1
	right = end

	while left <= right :
		while right > start and array[pivot] >= array[right] :
			right -= 1
		while left <= end and array[pivot] <= array[left] :
			left += 1

		if left > right :
			array[pivot], array[right] = array[right], array[pivot]
		else :
			array[left], array[right] = array[right], array[left]
		
	quick_sort(start, right-1, array)
	quick_sort(right+1, end, array)

quick_sort(0, len(array)-1, array)
print(array)

