import sys
input = sys.stdin.readline

def dfs(list, x1, y1, x2, y2):
    global b_cnt
    global w_cnt

    if x1 - x2 == 0 and y1 - y2 == 0:
        state = list[x1][y1]
        if state == 1:
            b_cnt += 1
        else:
            w_cnt += 1    
        return
    
    con_dfs = False
    state = list[x1][y1]
    
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            if list[i][j] != state:
                con_dfs = True
                break
        if con_dfs == True:
            break
        
    
    if con_dfs == True:
        xm = (x1 + x2) // 2
        ym = (y1 + y2) // 2
        dfs(list, x1, y1, xm, ym)
        dfs(list, x1, ym + 1, xm, y2)
        dfs(list, xm + 1, y1, x2, ym)
        dfs(list, xm + 1, ym + 1, x2, y2)
    else: # elif con_dfs == False
        if state == 1:
            b_cnt += 1
        else:
            w_cnt += 1
        return
            
n = int(input())
list = [list(map(int, input().split())) for i in range(n)]

b_cnt = 0
w_cnt = 0

dfs(list, 0, 0, n - 1, n - 1)

print(w_cnt)
print(b_cnt)
