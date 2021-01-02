import sys
X = int(sys.stdin.readline().rstrip())

array = [0] * 30001

def sol(X) :
	count = [X] * 4
	if array[X] != 0 :
		return array[X]
	
	if X == 1 :
		return 0

	if X%2 == 0 :
		count[0] = sol(X//2) + 1
	if X%3 == 0 :
		count[1] = sol(X//3) + 1
	if X%5 == 0 :
		count[2] = sol(X//5) + 1
	
	count[3]= sol(X-1) + 1
	array[X] = min(count)
	return array[X]


print(sol(X))