import sys
input = sys.stdin.readline

n = int(input())
step = [0]
for _ in range(n):
    step.append(int(input()))
if n == 1:
    print(step[1])
    exit()     
dp = [0] * 302
dp[1] = step[1]
dp[2] = dp[1] + step[2]
for i in range(3, n + 1):
    dp[i] = max(dp[i - 2], step[i - 1] + dp[i - 3]) + step[i]
print(dp[n])
