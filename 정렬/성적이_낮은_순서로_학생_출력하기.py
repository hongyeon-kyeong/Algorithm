import sys
N = int(sys.stdin.readline().rstrip())
array = []

for _ in range(N) :
	input_data = sys.stdin.readline().rstrip().split()
	#print(input_data)
	array.append((int(input_data[1]), input_data[0]))

#array = sorted(array, key = lambda x:x[0])
array=sorted(array)
for i in range(N) :
	print(array[i][1], end= ' ')