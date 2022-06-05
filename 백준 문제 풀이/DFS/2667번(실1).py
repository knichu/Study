import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().strip())))

idx = 2
cnt = 0
def dfs(x, y, idx):
    global cnt
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    if graph[x][y] == 0:
        return False
    if graph[x][y] == 1:
        cnt += 1
        graph[x][y] = idx
        dfs(x - 1, y, idx)
        dfs(x, y + 1, idx)
        dfs(x + 1, y, idx)
        dfs(x, y - 1, idx)
        return True
    return False
result = []
for i in range(n):
    for j in range(n):
        if dfs(i, j, idx) == True:
            result.append(cnt)
            idx += 1
            cnt = 0
result.sort()
print(len(result))
for i in result:
    print(i)
