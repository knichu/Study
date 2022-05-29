import sys
input = sys.stdin.readline
from collections import deque
INF = 1e9
n, k = map(int, input().split())
dp = [INF] * 100001
dp[n] = 0
q = deque([n])
while True:
    a = q.popleft()
    if a == k:
        print(dp[a])
        break
    if a < 100000 and dp[a + 1] == INF:
        dp[a + 1] = dp[a] + 1
        q.append(a + 1)
    if a <= 50000 and dp[a * 2] == INF:
        dp[a * 2] = dp[a] + 1
        q.append(a * 2)
    if a > 0 and dp[a - 1] == INF:
        dp[a - 1] = dp[a] + 1
        q.append(a - 1)
