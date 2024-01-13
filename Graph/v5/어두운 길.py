n, m = map(int, input().split())
edges = []
parent = [0] * (n+1)

for i in range(1, n+1):
    parent[i] = i

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

original_cost = 0
for _ in range(m):
    x, y, z = map(int, input().split())
    edges.append((z, x+1, y+1))
    original_cost += z

edges.sort()
optimized_cost = 0
for edge in edges:
    z, x, y = edge
    if find_parent(parent, x) != find_parent(parent, y):
        optimized_cost += z
        union_parent(parent, x, y)

print(original_cost - optimized_cost)


