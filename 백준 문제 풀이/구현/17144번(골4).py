# 17144번
import sys

input = sys.stdin.readline


def spread(x, y, graph, r, c):
    global tmp_graph
    spread_position = graph[x][y]
    spread_amount = spread_position // 5
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    spread_count = 0
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if nx < 0 or nx >= r or ny < 0 or ny >= c or graph[nx][ny] == -1:
            continue
        spread_count += 1
        tmp_graph[nx][ny] += spread_amount
    tmp_graph[x][y] -= spread_amount * spread_count


def circulation(down_pos, r, c):
    global graph
    global total
    down_x = down_pos
    up_x = down_x - 1
    up_tmp, next_up_tmp = 0, 0
    down_tmp, next_down_tmp = 0, 0
    up_tmp_idx, down_tmp_idx = 0, 0
    up_y, down_y = 0, 0
    up_tmp_max = (2 * c + (up_x - 1) * 2 - 1)
    down_tmp_max = (2 * c + (r - down_x - 2) * 2 - 1)

    # 위쪽 공기 순환
    up_dx = [0, -1, 0, 1]
    up_dy = [1, 0, -1, 0]
    for i in range(4):
        nx = up_x + up_dx[i]
        ny = up_y + up_dy[i]
        while 0 <= nx < r and 0 <= ny < c:
            if up_tmp_idx == up_tmp_max:
                break
            up_tmp = next_up_tmp
            next_up_tmp = graph[nx][ny]
            graph[nx][ny] = up_tmp
            up_tmp_idx += 1
            up_x, up_y = nx, ny
            nx = up_x + up_dx[i]
            ny = up_y + up_dy[i]
        nx = up_x
        ny = up_y
    total -= next_up_tmp
    
    # 아래쪽 공기 순환
    down_dx = [0, 1, 0, -1]
    down_dy = [1, 0, -1, 0]
    for i in range(4):
        nx = down_x + down_dx[i]
        ny = down_y + down_dy[i]
        while 0 <= nx < r and 0 <= ny < c:
            if down_tmp_idx == down_tmp_max:
                break
            down_tmp = next_down_tmp
            next_down_tmp = graph[nx][ny]
            graph[nx][ny] = down_tmp
            down_tmp_idx += 1
            down_x, down_y = nx, ny
            nx = down_x + down_dx[i]
            ny = down_y + down_dy[i]
        nx = down_x
        ny = down_y
    total -= next_down_tmp
    

# main
R, C, T = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(R)]
tmp_graph = [[0] * C for _ in range(R)]

# 초기 미세먼지 총량 맟 공기청정기 위치
total = 2
circulator_pos = 0
for i in range(R):
    for j in range(C):
        total += graph[i][j]
        if j == 0:
            if graph[i][j] == -1:
                circulator_pos = i

# 실제 작동
for _ in range(T):
    for i in range(R):
        for j in range(C):
            if graph[i][j] and graph[i][j] != -1:
                spread(i, j, graph, R, C)
    for i in range(R):
        for j in range(C):
            graph[i][j] += tmp_graph[i][j]
    tmp_graph = [[0] * C for _ in range(R)]

    circulation(circulator_pos, R, C)
    
print(total)


# 코멘트 : 카카오인턴문제처럼 링크드 리스트를 이용해서 쓰는 자원을 획기적으로 줄일수 있을꺼 같다. 현재 코드도 많이 느린편이니 다시 풀어 볼 것.
