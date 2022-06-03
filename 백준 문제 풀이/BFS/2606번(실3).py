import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [False] * (n + 1)
visited[1] = True
q = deque([1])
cnt = 0
while q:
    a = q.popleft()
    for i in graph[a]:
        if visited[i] == False:
            visited[i]= True
            cnt += 1
            q.append(i)
print(cnt)
