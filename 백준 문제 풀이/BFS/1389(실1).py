import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def finding(x):
    distance = [- 1] * (n + 1)
    distance[0] = 0
    distance[x] = 0
    q = deque([x])
    while q:
        a = q.popleft()
        for i in graph[a]:
            if distance[i] != - 1:
                continue
            else:
                distance[i] = distance[a] + 1
                q.append(i)
    return sum(distance)

lst = []
for i in range(1, n + 1):
    lst.append((finding(i), i))
print(min(lst)[1])
