import sys
input = sys.stdin.readline
from collections import deque

a, b = map(int, input().split())
graph = [list(input().strip()) for _ in range(a)]
visited = [[False] * b for _ in range(a)]
if (a + b) % 2 == 1:
    print("NO SOLUTION")
    exit()

def judge(x, y):
    if (x + y) % 2 == 0:
        if graph[x][y] == "\\":
            return True
        else:
            return False
    else:
        if graph[x][y] == "\\":
            return False
        else:
            return True

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
cnt = 0
if graph[a - 1][b - 1] == "/":
    cnt = 1
visited[0][0] = True
q = deque([(0, 0, cnt)])
while q:
    x, y, cnt = q.popleft()
    
    if x == a - 1 and y == b - 1:
        print(cnt)
        break
    
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx < 0 or nx >= a or ny < 0 or ny >= b:
            continue
        if visited[nx][ny] == True:
            continue
        if judge(nx, ny):
            visited[nx][ny] = True
            q.appendleft((nx, ny, cnt))
        elif not judge(nx, ny):
            visited[nx][ny] = True
            q.append((nx, ny, cnt + 1))
