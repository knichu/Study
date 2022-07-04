import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * (50001)
for i in range(1, n + 1):
    idx = 5
    cnt = 1
    while i >= cnt ** 2:
        ans = i - cnt ** 2
        idx = min(idx, dp[ans])
        cnt += 1
    dp[i] = idx + 1
print(dp[n])

# 그냥 pypy쓰면 될껄 파이썬으로 해보려다 시간날림. 시간짧은코드 보니까 DP로 안품.
