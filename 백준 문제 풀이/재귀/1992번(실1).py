import sys
input = sys.stdin.readline

n = int(input())
map = [list(input()) for _ in range(n)]
result = ""


def dfs(n, x, y):
    global result
    state = map[x][y]
    if n == 1:
        result += state
        return
    
    con_dfs = False
    for i in range(x, x + n):
        for j in range(y, y + n):
            if map[i][j] != state:
                con_dfs = True
                break
        if con_dfs == True:
            break
    
    if con_dfs == True:
        result += "("
        mx = x + n // 2
        my = y + n // 2
        
        dfs(n // 2, x, y)
        
        dfs(n // 2, x, my)
        
        dfs(n // 2, mx, y)
        
        dfs(n // 2, mx, my)
        result += ")"
        
    else: # elif con_dfs == False:
        result += state
        
dfs(n, 0, 0)

print(result)
