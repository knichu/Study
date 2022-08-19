import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * 3 for _ in range(n)]
dp[0] = [graph[0][0], graph[0][1], graph[0][2]]
for i in range(n - 1):
    dp[i + 1][0] = graph[i + 1][0] + min(dp[i][1], dp[i][2])
    dp[i + 1][1] = graph[i + 1][1] + min(dp[i][0], dp[i][2])
    dp[i + 1][2] = graph[i + 1][2] + min(dp[i][0], dp[i][1])
mn = min(dp[n - 1])
print(mn)
