from collections import deque
import copy

n = int(input())
hours = [0] * (n+1)
graph = [[] for i in range(1, n+1)]
indegree = [0] * (n+1)

for i in range(1, n+1):
    data = list(map(int, input().split()))
    hours[i] = data[0]
    for x in data[1:-1]:
        graph[x].append(i)
        indegree[i] += 1
def topology_sort() :
    result = copy.deepcopy(hours)
    q = deque()

    for i in indegree:
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        for i in graph[now]:
            indegree[i] -= 1
            hours[now] = max(result[i], hours[i] + result[now])
            if indegree[i] == 0:
                q.append(i)

    for i in range(1, n+1):
        print(result[i])

topology_sort()

