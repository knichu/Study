import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def solve(n, m, pic):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    t = -1
    
    def dfs(x, y):
        global flag
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if visited[nx][ny] == -1 or visited[nx][ny] == 2:
                continue
            
            if pic[nx][ny] == 0:
                visited[nx][ny] = -1
                dfs(nx, ny)
            else:
                flag = True
                visited[nx][ny] += 1
                if visited[nx][ny] == 2:
                    pic[nx][ny] -= 2
                    
    global flag
    flag = True
    while flag:
        flag = False
        visited = [[0] * m for _ in range(n)]
        visited[0][0] = -1 
        dfs(0, 0)
        for i in range(n):
            for j in range(m):
                if pic[i][j] == -1:
                    pic[i][j] += 1
        t += 1
    return print(t)

n, m = map(int, input().split())
pic = [list(map(int, input().split())) for _ in range(n)]
solve(n, m, pic)
