import sys

input = sys.stdin.readline


def solve(i, move_idx, turn, dx, dy):
    global sand_out
    global idx
    global graph
    global start_idx
    for _ in range(i):
        start_idx[0] += dx[idx]
        start_idx[1] += dy[idx]
        start_amount = graph[start_idx[0]][start_idx[1]]
        remove_amount = 0
        for j in move_idx:
            if turn[idx][2] == 0:
                nx = start_idx[0] + turn[idx][0] * j[0]
                ny = start_idx[1] + turn[idx][1] * j[1]
            else:
                nx = start_idx[0] + turn[idx][1] * j[1]
                ny = start_idx[1] + turn[idx][0] * j[0]
            rate = (start_amount * j[2]) // 100
            if 0 <= nx < n and 0 <= ny < n:
                graph[nx][ny] += rate
            else:
                sand_out += rate
            remove_amount += rate
        nx = start_idx[0] + dx[idx]
        ny = start_idx[1] + dy[idx]
        if 0 <= nx < n and 0 <= ny < n:
            graph[nx][ny] += start_amount - remove_amount
        else:
            sand_out += start_amount - remove_amount
        graph[start_idx[0]][start_idx[1]] = 0


n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

# 서 남 동 북 순서, 서쪽 부터 시작
move_idx = [[0, -2, 5],
            [-1, -1, 10],
            [1, -1, 10],
            [-2, 0, 2],
            [-1, 0, 7],
            [1, 0, 7],
            [2, 0, 2],
            [-1, 1, 1],
            [1, 1, 1]]

# if turn[i][3] == 1: x y 자리 바꾸기
turn = [[1, 1, 0], [1, -1, 1], [1, -1, 0], [1, 1, 1]]
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

idx = 0
sand_out = 0
start_idx = [n // 2, n // 2]

for i in range(1, n):
    solve(i, move_idx, turn, dx, dy)
    idx += 1
    solve(i, move_idx, turn, dx, dy)
    idx += 1
    if idx >= 3:
        idx = 0
solve(n, move_idx, turn, dx, dy)

print(sand_out)


# 코멘트 : 전날에 정신이 나갔었나봄. 바로 수정해서 제출함
