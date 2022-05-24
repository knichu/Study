import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
graph = [[0] * n for i in range(n)]
graph[0][0] = 9
for _ in range(int(input())):
    a, b = map(int, input().split())
    graph[a - 1][b - 1] = 1
com_list = []
l = int(input())
for _ in range(l):
    a, b = input().split()
    com_list.append([int(a), b])

com_index = 0
com_time = com_list[0][0] # 3
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
d_state = 0
time = 1
x, y = 0, 0
graph_q = deque()
graph_q.append([0, 0])

while True:
    if com_time == 0:
        com_index += 1
        if com_index != l:
            com_time = com_list[com_index][0] - com_list[com_index - 1][0]
            if com_list[com_index - 1][1] == "L":
                d_state -= 1
                if d_state == -1:
                    d_state = 3
            else: # com_list[com_index][1] == "D":
                d_state += 1
                if d_state == 4:
                    d_state = 0
                
        else: # elif com_index == l:
            com_time = 101
            if com_list[com_index - 1][1] == "L":
                d_state -= 1
                if d_state == -1:
                    d_state = 3
            else: # com_list[com_index][1] == "D":
                d_state += 1
                if d_state == 4:
                    d_state = 0
    
    nx = x + dx[d_state]
    ny = y + dy[d_state]
    
    if nx < 0 or nx >= n or ny < 0 or ny >= n:
        break
    if graph[nx][ny] == 9:
        break
    elif graph[nx][ny] == 1:
        x = nx
        y = ny
        graph[x][y] = 9
        graph_q.append([x, y])
    else: # graph[nx][ny] == 0:
        x = nx
        y = ny
        graph[x][y] = 9
        graph_q.append([x, y])
        a, b = graph_q.popleft()
        graph[a][b] = 0
        
    time += 1
    com_time -= 1
    
print(time)
