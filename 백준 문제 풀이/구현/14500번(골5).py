import sys
input = sys.stdin.readline

def dfs(x, y, cnt, mx):
    global lar
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if visited[nx][ny] == False:
                if cnt < 3:
                    visited[nx][ny] = True
                    dfs(nx, ny, cnt + 1, mx + graph[nx][ny])
                    visited[nx][ny] = False
                elif cnt >= 3:
                    lar = max(mx + graph[nx][ny], lar)
                    continue
    return lar

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0
for i in range(n):
    for j in range(m):
        lar = 0
        visited[i][j] = True
        result = max(result, dfs(i, j, 1, graph[i][j]))
        visited[i][j] = False

for i in range(1, n - 1):
    for j in range(m):
        k = graph[i - 1][j] + graph[i][j] + graph[i + 1][j]
        if j == 0:
            result = max(result, k + graph[i][j + 1])
        elif j == (m - 1):
            result = max(result, k + graph[i][j - 1])
        else:
            result = max(result, k + graph[i][j + 1])
            result = max(result, k + graph[i][j - 1])

for i in range(n):
    for j in range(1, m - 1):
        k = graph[i][j - 1] + graph[i][j] + graph[i][j + 1]
        if i == 0:
            result = max(result, k + graph[i + 1][j])
        elif i == (n - 1):
            result = max(result, k + graph[i - 1][j])
        else:
            result = max(result, k + graph[i + 1][j])
            result = max(result, k + graph[i - 1][j])

print(result)
