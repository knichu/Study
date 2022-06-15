import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    dp = [1] * 101
    dp[0] = 0
    dp[4] = 2
    if n < 5:
        print(dp[n])
    else:
        for i in range(5, n + 1):
            dp[i] = dp[i - 1] + dp[i - 5]
        print(dp[n])
