import sys
input = sys.stdin.readline
from collections import deque

a, b = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(a)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
q = deque([(0, 0)])
while graph[a - 1][b - 1] == 1:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]    
        if nx < 0 or nx >= a or ny < 0 or ny >= b:
            continue
        if graph[nx][ny] == 0:
            continue
        if graph[nx][ny] == 1:
            graph[nx][ny] = graph[x][y] + 1
            q.append((nx, ny))
print(graph[a - 1][b - 1])
