import sys
input = sys.stdin.readline

g = int(input())
p = int(input())

visited = [False] * (g+1)
count = 0
gates = []

for _ in range(p) :
	gates.append(int(input()))
	
for gate in gates :	
	chk = False
	if not visited[gate] :
		visited[gate] = True
		count+=1
		chk = True
	else :
		for i in range(gate-1,0,-1) :
			if not visited[i] :
				visited[i] = True
				count+=1
				chk = True
				break
	print(gate, count)
	if not chk :
		break

print(count)

'''
4
3
4
1
1

4
6
2
2
3
3
4
4

'''


