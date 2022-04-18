import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(input()) for i in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    if graph[x][y] == "W":
        return 0
    max_dist = 0
    visit = [[-1] * m for i in range(n)]
    visit[x][y] = 0
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == "W":
                continue
            if visit[nx][ny] == -1:
                visit[nx][ny] = visit[x][y] + 1
                max_dist = max(max_dist, visit[nx][ny])
                queue.append((nx, ny))
    return max_dist

result = 0
for i in range(n):
    for j in range(m):
        result = max(result, bfs(i, j))

print(result)
