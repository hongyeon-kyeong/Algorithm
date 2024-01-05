n = int(input())
parent = [0] * 100001
parent[1] = 1

for i in range(n-1):
    x, y = map(int, input().split())
    if parent[y] != 0 or y == 1:
        parent[x] = y
    else:
        parent[y] = x

for i in range(2,n+1):
    if parent[i] != 0:
        print(parent[i])