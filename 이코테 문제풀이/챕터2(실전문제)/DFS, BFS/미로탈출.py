# 내가 작성한 코드(답안예시참고)

from collections import deque

n, m = map(int, input().split())

maze = [list(map(int, input())) for i in range(n)]

dx = [-1, 0, 1, 0]  # 상, 우, 하, 좌
dy = [0, 1, 0, -1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    

    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
        
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
        
            if maze[nx][ny] == 0:
                continue
            
            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                q.append((nx, ny))
                
    return maze[n-1][m-1]
        
print(bfs(0, 0))
    

  
# 좀더 형태에 익숙해지고 체화시켜야 할꺼 같다.
