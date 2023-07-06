import sys
from collections import deque
input = sys.stdin.readline


# 길찾기 bfs
def bfs(a, b, n, m):
    global tmp_graph
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    q = deque()
    q.append((a, b))
    tmp_graph[a][b] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if tmp_graph[nx][ny] != 0:
                continue
            tmp_graph[nx][ny] = 1
            q.append((nx, ny))


N, M = map(int, input().split())
graph = [list(map(int, list(str(input().strip())))) for _ in range(N)]
visited_graph = [[0] * M for _ in range(N)]

total = 0

for height in range(9, 0, -1):
    tmp_graph = [[0] * M for _ in range(N)]
    flag = True
    # 각 높이 별 막혀있는 부분 구하기
    for i in range(N):
        for j in range(M):
            if graph[i][j] >= height:
                visited_graph[i][j] = 1
                tmp_graph[i][j] = 1
            else:
                flag = False
    if flag:
        break

    # 가장자리만 bfs 돌리기
    for x in range(N):
        if tmp_graph[x][0] == 0:
            bfs(x, 0, N, M)

    for x in range(N):
        if tmp_graph[x][M - 1] == 0:
            bfs(x, M - 1, N, M)

    for y in range(M):
        if tmp_graph[0][y] == 0:
            bfs(0, y, N, M)

    for y in range(M):
        if tmp_graph[N - 1][y] == 0:
            bfs(N - 1, y, N, M)

    flag = False
    # 가장자리랑 이어저있지 않은 부분 부하기
    for i in range(N):
        for j in range(M):
            # visited_graph[i][j] == 0 는 가장자리랑 맞닿아 있진 않으나 이미 방문처리된 부분 구별
            if tmp_graph[i][j] == 0 and visited_graph[i][j] == 0:
                total += height - graph[i][j]
                visited_graph[i][j] = 1

print(total)


# 코멘트 : 처음에 재대로 생각했지만 그 방법이 최선인지를 고민을 좀 했다. 바로 구현했으면 20분도 안걸릴 문제.
