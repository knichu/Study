from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(input()) for i in range(n)]
coin = []
for i in range(n):
    for j in range(m):
        if len(coin) == 2:
            break
        if graph[i][j] == "o":
            coin.append((i, j))
x1, y1 = coin[0]
x2, y2 = coin[1]
count = 0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
    
def bfs(x1, y1, x2, y2, count):
    q = deque()
    q.append((x1, y1, x2, y2, count))
    while q:
        if count >= 10:
            return -1
        x1, y1, x2, y2, count = q.popleft()
        for i in range(4):
            nx = x1 + dx[i]
            ny = y1 + dy[i]
            mx = x2 + dx[i]
            my = y2 + dy[i]
            if 0 <= nx < n and 0 <= ny < m and 0 <= mx < n and 0 <= my < m:
                if graph[nx][ny] == "#":
                    nx, ny = x1, y1
                if graph[mx][my] == "#":
                    mx, my = x2, y2
                q.append((nx, ny, mx, my, count + 1))
            elif 0 <= nx < n and 0 <= ny < m:
                return count + 1
            elif 0 <= mx < n and 0 <= my < m:
                return count + 1
            else:
                continue
    return -1
                
print(bfs(x1, y1, x2, y2, count))
