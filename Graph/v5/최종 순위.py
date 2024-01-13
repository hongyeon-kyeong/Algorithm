from collections import deque

x = int(input())
for _ in range(x):
    n = int(input())
    graph = [[0] * (n+1) for _ in range(n+1)]
    data = list(map(int, input().split()))
    for i in range(n):
        for j in range(i+1, n):
            graph[data[i]][data[j]] = 1

    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a][b], graph[b][a] = graph[b][a], graph[a][b]

    for i in range(1, n+1):
        for j in range(1, n+1):
            print(graph[i][j], end='')
        print()

    indegree = [0] * (n+1)
    for i in range(1, n+1):
        for j in range(1, n+1):
            if graph[i][j] == 1:
                indegree[j] += 1

    q = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    cycle = False
    certain = True
    result = []

    for i in range(n):

        if len(q) == 0:
            cycle = True
            break

        if len(q) >= 2:
            certain = False
            break

        now = q.popleft()
        result.append(now)
        for j in range(1, n+1):
            if graph[now][j] == 1:
                indegree[j] -= 1
                if indegree[j] == 0:
                    q.append(j)

    if cycle:
        print('IMPOSSIBLE')
    elif not certain:
        print('?')
    else:
        for i in result:
            print(i, end=' ')
        print()
