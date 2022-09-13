import sys
input = sys.stdin.readline
from collections import deque
inf = float("inf")

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
                      
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == land_index:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = land_index
                q.append((nx, ny))  
                 
    land_index += 1
    return

def get_all_bridge(x, y):
    k = graph[x][y]
    if k == 0:
        return 
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
                    
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if graph[nx][ny] == land_index:
            continue
        bridge_length = 0
        while True:
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                break
            if graph[nx][ny] == 0:
                nx += dx[i]
                ny += dy[i]
                bridge_length += 1
            else:
                l = graph[nx][ny]
                break
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if bridge_length >= 2:
            all_Bridge[k][l] = min(all_Bridge[k][l], bridge_length)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# main
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
land_index = 2
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(n):
    for j in range(m):
        change_land_index(i, j)

all_Bridge = [[inf] * land_index for _ in range(land_index)]
for i in range(n):
    for j in range(m):
        get_all_bridge(i, j)

edges = []
for i in range(2, land_index):
    for j in range(i + 1, land_index):
        if all_Bridge[i][j] != inf:
            edges.append((all_Bridge[i][j], i, j))
edges.sort()

parent = []
for i in range(land_index):
    parent.append(i)

total_cost = 0
count_bridge = 0
for i in range(len(edges)):
    if count_bridge == (land_index - 3):
        break
    cost, a, b = edges[i]
    if find(a) != find(b):
        union(a, b)
        total_cost += cost
        count_bridge += 1

flag = True
for i in range(2, land_index):
    if find(i) != 2:
        flag = False
if flag:
    print(total_cost)
else:
    print(-1)
