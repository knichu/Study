import sys
input = sys.stdin.readline

def dragon_curve(x, y, d, g):
    graph[x][y] = True
    nx = x + dx[d]
    ny = y + dy[d]
    graph[nx][ny] = True
    lst = [(x, y), (nx, ny)]
    
    for _ in range(g):
        pivot_x, pivot_y = lst[-1]
        for i in range(len(lst) - 1, -1, -1):
            new_x = - lst[i][1] + pivot_x + pivot_y
            nex_y = lst[i][0] - pivot_x + pivot_y
            graph[new_x][nex_y] = True
            lst.append((new_x, nex_y))

n = int(input())
graph = [[False] * 101 for _ in range(101)]
curve = []
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
for i in range(n):
    x, y, d, g = map(int, input().split())
    dragon_curve(x, y, d, g)

cnt = 0
for i in range(100):
    for j in range(100):
        if graph[i][j]:
            if graph[i + 1][j] and graph[i][j + 1] and graph[i + 1][j + 1]:
                cnt += 1
print(cnt)
