import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
ladder = [0] * 101
for _ in range(n + m):
    a, b = map(int, input().split())
    ladder[a] = b
dp = [0] * 101
q = deque()
q.append(1)
while q:
    now = q.popleft()
    if now == 100:
        print(dp[now])
        break
    for dice in range(1, 7):
        next = now + dice
        if next > 100:
            continue
        j = ladder[next]
        if j != 0:
            next = j
        if dp[next] == 0:
            dp[next] = dp[now] + 1
            q.append(next)
