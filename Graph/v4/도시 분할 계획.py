import sys
input = sys.stdin.readline

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

n, m = map(int, input().split())
edges = []
parent = [0] * (n+1)

for i in range(0, n+1):
    parent[i] = i

for i in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()
result = 0
final_edge = 0
for edge in edges:
    c, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += c
        final_edge = c

print(result - final_edge)
