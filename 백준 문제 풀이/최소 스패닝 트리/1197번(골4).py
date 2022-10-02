import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return (parent[x])

def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

v, e = map(int, input().split())
edges = []
for _ in range(e):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))
edges.sort()

parent = [i for i in range(v + 1)]

total = 0
cnt = 0
for i in edges:
    cost, x, y = i
    if find(x) != find(y):
        total += cost
        union(x, y)
        cnt += 1
    if cnt == v - 1:
        break

print(total)
