import sys
input = sys.stdin.readline

def solve(x):
    if x == len(fill):
        return False
    
    i, j = fill[x]
    ck_set = [True] + [False] * 9
    a, b = i // 3, j // 3
    for p in range(a * 3, (a + 1) * 3):
        for q in range(b * 3, (b + 1) * 3):
            ck_set[sudoku[p][q]] = True
    
    for k in range(9):
        ck_set[sudoku[i][k]] = True
        ck_set[sudoku[k][j]] = True

    for k in range(1, 10):
        if not ck_set[k]:
            sudoku[i][j] = k
            flag = solve(x + 1)
            if not flag:
                return False
            sudoku[i][j] = 0
    return True
    
sudoku = [list(map(int, list(input().rstrip()))) for _ in range(9)]
fill = []
for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            fill.append((i, j))
solve(0)
for i in range(9):
    for j in range(9):
        print(sudoku[i][j], end = "")
    print()
    
    
    
    
# 코멘트 : sys.setrecursionlimit(int(1e6)) 이 한줄 추가해서 계속 메모리 초과가 떳다.
