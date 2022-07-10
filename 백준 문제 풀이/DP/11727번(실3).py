import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * (1001)
dp[1], dp[2] = 1, 3
for i in range(3, n + 1):
    dp[i] =  2 * dp[i - 2] + dp[i - 1]
print(dp[n] % 10007)
