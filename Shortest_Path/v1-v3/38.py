import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

# i가 찌르는 리스트
graph_a = [[] for _ in range(n+1)]

# i를 찌르는 리스트
graph_b = [[] for _ in range(n+1)]

for _ in range(m) :
	a, b = map(int, input().split())
	graph_a[a].append(b)
	graph_b[b].append(a)

res = 0
for i in range(1,n+1) :
	q_a = deque()
	q_a.append(i)
	count_a = 0
	q_b = deque()
	count_b = 0
	q_b.append(i)
	visited_a = [False] * (n+1)
	visited_b = [False] * (n+1)

	while q_a :
		now = q_a.popleft()
		visited_a[now] = True
		for v in graph_a[now] :
			if not visited_a[v] :
				q_a.append(v)
				count_a += 1

	while q_b :
		now = q_b.popleft()
		visited_b[now] = True
		for v in graph_b[now] :
			if not visited_b[v] :
				q_b.append(v)
				count_b += 1

	if count_a + count_b == n-1 :
		res += 1	

print(res)
# 노드마다 queue를 사용해서 내가 찌르는 노드 수와 나를 찌르는 노드 수의 합

# 합이 전체 노드수 -1 인 노드만 카운트