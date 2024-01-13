n, m = map(int, input().split())
parent = [0] * (n+1)

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for i in range(1, n+1):
    parent[i] = i

graph = [[] for i in range(n+1)]
for i in range(1, n+1):
    data = list(map(int, input().split()))
    for j in range(0, n):
        if data[j] == 1:
            union_parent(parent, i, j+1)

plans = list(map(int, input().split()))

result = False
for i in range(m-1):
    if find_parent(parent, plans[i]) != find_parent(parent, plans[i+1]) :
        break
    result = True

print(result)