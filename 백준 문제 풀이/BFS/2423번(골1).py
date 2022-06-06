import sys
input = sys.stdin.readline
from collections import deque
INF = int(1e9)

a, b = map(int, input().split())
graph = [list(input().strip()) for _ in range(a)]
if (a + b) % 2 == 1:
    print("NO SOLUTION")
    exit()
    
for i in range(a):
    for j in range(b):
            if (i + j) % 2 == 0:
                if graph[i][j] == "\\":
                    graph[i][j] = 0
                else:
                    graph[i][j] = 1
            else:
                if graph[i][j] == "\\":
                    graph[i][j] = 1
                else:
                    graph[i][j] = 0
   
visited = [[INF] * (b) for _ in range(a)]

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

visited[0][0] = graph[0][0]
q = deque([(0, 0, graph[0][0])])
while q:
    x, y, cnt = q.popleft()
    
    if x == (a - 1) and y == (b - 1):
        print(cnt)
        break
    
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= a or ny < 0 or ny >= b:
            continue
        if (nx + ny) % 2 == 0:
            if i == 1 or i == 5:
                continue
        else: # elif (x + y) % 2 == 1:
            if i == 3 or i == 7:
                continue
        if visited[nx][ny] != INF:
            continue
        
        if graph[nx][ny] == 0:
            q.appendleft((nx, ny, cnt))
            visited[nx][ny] = cnt
            if nx == (a - 1) and ny == (b - 1):
                print(cnt)
                exit()
        else: # elif graph[nx][ny] == 1:
            q.append((nx, ny, cnt + 1))
            visited[nx][ny] = cnt + 1
            if nx == (a - 1) and ny == (b - 1):
                print(cnt + 1)
                exit()
