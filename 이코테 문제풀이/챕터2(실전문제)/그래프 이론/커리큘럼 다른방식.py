from collections import deque

n = int(input())  # n = 5

indegree = [0] * (n + 1)

graph = [[] for i in range(n + 1)]

time = [] * (n + 1)

for i in range(1, n + 1):
    k = list(map(int, input().split()))
    time[i] = k[0]
    l = len(k)
    for j in range(1, l-1):
        graph[i].append(k[j])
        indegree[i] += 1      


# time = [0, 10, 10, 4, 4, 3]

q = deque()
result_time = 0

def dfs(graph, start):
    q.appendleft(start)
    result_time += time[start + 1]
    a = q.popleft()
    for i in graph[a]:
        if not graph[i]:
            continue
