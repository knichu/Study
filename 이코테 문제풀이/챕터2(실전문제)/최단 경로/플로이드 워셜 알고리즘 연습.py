import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())

graph = [[INF] * (n + 1) for i in range(n + 1)]

for i in range(n + 1):
    graph[i][i] = 0

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

for x in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][x] + graph[x][j])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(graph[i][j], end = ' ')
    print()
