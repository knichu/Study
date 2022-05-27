import sys
input = sys.stdin.readline
from collections import deque

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
for i in graph:
    i.sort()

visited = [False] * (n + 1)

def dfs(x, visited):
    visited[x] = True
    print(x, end=' ')
    for i in graph[x]:
        if not visited[i]:
            dfs(i, visited)
dfs(v, visited)
print()

visited = [False] * (n + 1)

def bfs(x, visited):
    q = deque()
    q.append(x)
    visited[x] = True
    while q:
        a = q.popleft()
        print(a, end=' ')
        for i in graph[a]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
bfs(v, visited)
