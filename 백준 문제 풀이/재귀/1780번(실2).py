import sys
input = sys.stdin.readline

n = int(input())
map = [list(map(int, input().split())) for _ in range(n)]
result = [0, 0, 0]

def dfs(n, x, y):
    state = map[x][y]
    if n == 1:
        result[state] += 1
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
        x1 = x + n // 3
        x2 = x1 + n // 3
        y1 = y + n // 3
        y2 = y1 + n // 3
        
        
        dfs(n // 3, x, y)
        dfs(n // 3, x, y1)
        dfs(n // 3, x, y2)
        
        dfs(n // 3, x1, y)
        dfs(n // 3, x1, y1)
        dfs(n // 3, x1, y2)
        
        dfs(n // 3, x2, y)
        dfs(n // 3, x2, y1)
        dfs(n // 3, x2, y2)
        
    else: # elif con_dfs == False
        result[state] += 1
        return
        
dfs(n, 0, 0)

print(result[-1])
print(result[0])
print(result[1])
