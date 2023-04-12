import sys
input = sys.stdin.readline
INF = int(1e9)


n, m, r = map(int, input().split())
node = list(map(int, input().split()))
graph = [[INF] * n for _ in range(n)]
for i in range(n):
    graph[i][i] = 0
for _ in range(r):
    a, b, l = map(int, input().split())
    if graph[a - 1][b - 1] > l:
        graph[a - 1][b - 1] = l
        graph[b - 1][a - 1] = l
for x in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][x] + graph[x][j])
ans = 0
for i in range(n):
    sum = 0
    for j in range(n):
        if graph[i][j] <= m:
            sum += node[j]
    ans = max(ans, sum)
print(ans)

# 코멘트 : 그냥 플로이드 워셜.
