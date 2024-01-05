from collections import deque

queue = deque()
n = int(input())
data = [[0] * (n + 1) for _ in range(n + 1)]
a, b = map(int, input().split())
m = int(input())

visited = [[False] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    data[x][y] = 1
    data[y][x] = 1


def solve(e1, e2):
    queue.append((e1, 0))
    visited[e1][e1] = True

    while queue:
        k, count = queue.popleft()
        if k == e2:
            return count
        for i in range(1, n + 1):
            if data[k][i] == 1 and not visited[k][i]:
                queue.append((i, count + 1))
                visited[k][i] = True

    return -1


print(solve(a, b))

# 9
# 1 9
# 7
# 1 2
# 1 3
# 2 7
# 2 8
# 2 9
# 4 5
# 4 6
