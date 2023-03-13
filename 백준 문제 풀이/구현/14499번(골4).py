import sys

input = sys.stdin.readline


def CopyBottom(dice_record, x, y, graph):
    if graph[x][y] == 0:
        if dice_record[5] != 0:
            graph[x][y] = dice_record[5]
    else:
        dice_record[5] = graph[x][y]
        graph[x][y] = 0
    return dice_record, graph


def DiceMovingAndPrint(way, n, m, x, y, move_dice, dice_record, dx, dy, graph):
    way -= 1
    nx = x + dx[way]
    ny = y + dy[way]
    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        return x, y, dice_record, graph

    temp_dice_record = []
    for i in range(6):
        temp_dice_record.append(dice_record[move_dice[way][i]])
    temp_dice_record, graph = CopyBottom(temp_dice_record, nx, ny, graph)
    print(temp_dice_record[0])

    return nx, ny, temp_dice_record, graph


dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
move_dice = [[2, 0, 5, 3, 4, 1],
             [1, 5, 0, 3, 4, 2],
             [4, 1, 2, 0, 5, 3],
             [3, 1, 2, 5, 0, 4]]
dice_record = [0 for _ in range(6)]

n, m, x, y, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
# 동쪽은 1, 서쪽은 2, 북쪽은 3, 남쪽은 4
command = list(map(int, input().split()))

for way in command:
    x, y, dice_record, graph = \
        DiceMovingAndPrint(way, n, m, x, y, move_dice, dice_record, dx, dy, graph)
