from collections import deque
import sys
input = sys.stdin.readline

m, n, h = map(int, input().split())
stk = []
graph = [[] for _ in range(h)]
for i in range(h):
    for j in range(n):
        chk = list(map(int, input().split()))
        graph[i].append(chk)
        for k in range(m):
            if chk[k] == 1:
                stk.append((i, j, k, 0))

dx = [-1, 0, 1, 0, 0, 0]
dy = [0, 1, 0, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

def bfs(lst):
    global real_time
    q = deque()
    for i in lst:
        q.append(i)
    while q:
        c, b, a, time = q.popleft()
        real_time = time
        for i in range(6):
            nx = a + dx[i]
            ny = b + dy[i]
            nz = c + dz[i]
            if nx >= m or nx < 0 or ny >= n or ny < 0 or nz >= h or nz < 0:
                continue
            if graph[nz][ny][nx] == 1 or graph[nz][ny][nx] == -1:
                continue
            graph[nz][ny][nx] = 1
            q.append((nz, ny, nx, time + 1))
    return real_time

real_time = 0          
t = bfs(stk)

for i in range(h): # 높이
    for j in range(n): # 세로
        for k in range(m): # 가로
            if graph[i][j][k] == 0:
                print(-1)
                exit()
print(t)
