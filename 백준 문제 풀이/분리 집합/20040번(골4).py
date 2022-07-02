import sys
input = sys.stdin.readline

def find(x):
    while x != parent[x]:
        x = parent[x]
    return x

def union(x, y):
    global cnt
    cnt += 1
    a = find(x)
    b = find(y)
    if a < b:
        parent[b] = a
        return False
    elif a > b:
        parent[a] = b
        return False
    else:
        parent[a] = b
        return True

n, m = map(int, input().split())
parent = [i for i in range(n)]
cnt = 0
state = False
for _ in range(m):
    x, y = map(int, input().split())
    if state:
        continue
    if union(x, y):
        save = cnt
        state = True
if state:
    print(save)
else:
    print(0)
