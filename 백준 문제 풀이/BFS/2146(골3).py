import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
graph = [list(map(int, input().split())) for i in range(n)]
land_index = 2
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def change_land_index(a, b):
    k = graph[a][b]
    if k == 0 or k != 1:
        return 
    
    global land_index
    q = deque()
    q.append((a, b))
    
    while q:
        x, y = q.popleft()
        graph[x][y] = land_index
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
                      
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == land_index:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = land_index
                q.append((nx, ny))  
                 
    land_index += 1
    return

for i in range(n):
    for j in range(n):
        change_land_index(i, j)

bridge_length = 987654321

def bfs(a, b):
    k = graph[a][b]
    if k == 0:
        return 987654321
    
    global dx
    global dy
    
    q = deque()
    q.append((a, b, 0))
    visited = [[False] * n for i in range(n)]
    visited[a][b] = True
    
    while q:
        x, y, l = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
                      
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if visited[nx][ny] == True:
                continue
            if graph[nx][ny] == k:
                continue
            
            if graph[nx][ny] == 0:                
                visited[nx][ny] = True
                q.append((nx, ny, l + 1))
                
            elif graph[nx][ny] != 0: # 나중에 else: 로 바꾸기
                return l
    return 987654321
            
for i in range(n):
    for j in range(n):
        z = bfs(i, j)
        bridge_length = min(bridge_length, z)

print(bridge_length)
