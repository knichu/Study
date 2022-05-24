import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x, y):
    if x < 0 or x >= m or y < 0 or y >= n:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x + 1, y)
        dfs(x, y - 1)
        return True
    return False

for _ in range(int(input())):
    m, n, k = map(int, input().split())
    graph = [[0] * n for _ in range(m)]
    for _ in range(k):
        a, b = map(int, input().split())
        graph[a][b] = 1
    cnt = 0
    for i in range(m):
        for j in range(n):
            if dfs(i, j) == True:
                cnt += 1
    print(cnt)
