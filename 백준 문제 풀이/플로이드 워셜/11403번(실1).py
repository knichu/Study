import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
for x in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1 or (graph[i][x] == 1 and graph[x][j] == 1):
                graph[i][j] = 1
for i in range(n):
    for j in range(n):
        print(graph[i][j], end = ' ')
    print()
