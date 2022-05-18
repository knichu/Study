import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
graph = [[] for i in range(n + 1)]
for i in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False for i in range(n + 1)]
visited[1] = True

line = 0

q = deque()
q.append((1, 0))
while q:
    k, depth = q.popleft()
    if k != 1:
        if len(graph[k]) == 1:
            continue
    for i in graph[k]:
        if visited[i] == False:
            line += 1
            q.append((i, depth + 1))
            visited[i] = True
    line += depth * (len(graph[k]) - 2)
            
if line % 2 == 0:
    print("No")
else:
    print("Yes")
