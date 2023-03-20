import sys

input = sys.stdin.readline


def solve(n):
    if n % 2 == 1:
        return 0
    if n == 2:
        return 3
    if n == 4:
        return 11
    dp = [0] * (n // 2)
    dp[0], dp[1] = 3, 11
    for i in range(2, n // 2):
        dp[i] = dp[i - 1] * 4 - dp[i - 2]
    return dp[n // 2 - 1]


n = int(input())
print(solve(n))


# 코멘트 : dp 연습 더 해야겠다.
