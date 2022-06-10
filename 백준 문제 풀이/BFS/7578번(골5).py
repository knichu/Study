from collections import deque
import sys
input = sys.stdin.readline

m, n= map(int, input().split())
stk = []
graph = []
for j in range(n):
    chk = list(map(int, input().split()))
    graph.append(chk)
    for k in range(m):
        if chk[k] == 1:
            stk.append((j, k, 0))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(lst):
    global real_time
    q = deque()
    for i in lst:
        q.append(i)
    while q:
        b, a, time = q.popleft()
        real_time = time
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx >= m or nx < 0 or ny >= n or ny < 0:
                continue
            if graph[ny][nx] == 1 or graph[ny][nx] == -1:
                continue
            graph[ny][nx] = 1
            q.append((ny, nx, time + 1))
    return real_time

real_time = 0          
t = bfs(stk)
for j in range(n): # 세로
    for k in range(m): # 가로
        if graph[j][k] == 0:
            print(-1)
            exit()
print(t)
