import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(input().strip()))

def normal(x, y, z):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    if graph[x][y] == z:
        if visited[x][y] == False:
            visited[x][y] = True
            normal(x + 1, y, z)
            normal(x - 1, y, z)
            normal(x, y + 1, z)
            normal(x, y - 1, z)
            return True
    return False
    
count = 0
visited = [([False] * n) for _ in range(n)]
for i in range(n):
    for j in range(n):
        k = graph[i][j]
        if normal(i, j, k) == True:
            count += 1
print(count, end = " ")

for i in range(n):
    for j in range(n):
        if graph[i][j] == "G":
            graph[i][j] = "R"

count = 0
visited = [([False] * n) for _ in range(n)]
for i in range(n):
    for j in range(n):
        k = graph[i][j]
        if normal(i, j, k) == True:
            count += 1
print(count)
