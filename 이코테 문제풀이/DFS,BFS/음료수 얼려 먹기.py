# 내가 작성한 코드(답안 예시를 봐버림..)

n, m  = map(int, input().split())

ice_maker = [list(map(int, input().split())) for i in range(n)]

def dfs(x, y):
    
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    
    if ice_maker[x][y] == 0:
        ice_maker[x][y] = 1
        
        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)
        return True
    return False

count = 0

for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            count += 1
            
print(count)



# 코멘트

문제해결위한 아이디어가 잘 생각이 안났다.
