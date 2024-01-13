n = int(input())
planets = []
parent = [0] * (n+1)

for i in range(n):
    parent[i] = i

for _ in range(n):
    x, y, z = map(int, input().split())
    planets.append((x, y, z))

edges = []
for i in range(n):
    xi, yi, zi = planets[i]
    for j in range(n):
       xj, yj, zj = planets[j]
       if j > i:
        distance = min(abs(xi-xj), abs(yi-yj), abs(zi-zj))
        edges.append((distance, i, j))

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

edges.sort()
result = 0
for edge in edges:
    distance, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        result += distance
        union_parent(parent, a, b)

print(result)

