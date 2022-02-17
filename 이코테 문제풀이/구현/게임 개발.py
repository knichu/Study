n, m = map(int, input().split()) # n - A, m - B

x, y, d = map(int, input().split())

w = [(0, -1, -1), (-1, 0, 0), (0, 1, 1), (1, 0, 2), (0, -1, 3)] # 서, 북, 동, 남, 서. 3번째 원소는 방향 부여

map = [list(map(int, input().split())) for i in range(n)]
map[x][y] = 2
stay_count = 0
nx = 0
ny = 0

while True:
    for (i, j, k) in w:
        if w[k + 1] == d:   # d = 0 이면 (0, -1, -1) 서쪽 방향
            if d == 0:
                d = 3    # d = 0 -> d = 3
            else:
                d -= 1
            nx = x + i   # nx = 1 + (0) = 1
            ny = y + j   # ny = 1 + (-1) = 0
            if map[nx][ny] == 1 or map[nx][ny] == 2:
                stay_count += 1
                continue
            else:
                x = nx
                y = ny
                map[x][y] = 2
                stay_count = 0
                
        if stay_count >= 4:
            break
        else:
            continue

result = 0

for i in range(n):
    for j in range(m):
        if map[i][j] == 2:
            count += 1
        else:
            continue
        
print(result)
