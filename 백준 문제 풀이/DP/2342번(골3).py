import sys
input = sys.stdin.readline
inf = float('inf')

def get_add(lr, k):
    if k == 0:
        return 2
    elif k == lr:
        return 1
    elif abs(k - lr) == 1 or abs(k - lr) == 3:
        return 3
    else:
        return 4

note = list(map(int, input().split()))
n = len(note) - 1
if n == 0:
    print(0)
    exit()

dp = [[[inf for _ in range(5)] for _ in range(5)] for _ in range(n + 1)]
dp[-1][0][0] = 0

for i in range(n):
    for r in range(5):
        for k in range(5):
            add = get_add(note[i], k)
            dp[i][note[i]][r] = min(dp[i][note[i]][r], dp[i - 1][k][r] + add)

    for l in range(5):
        for k in range(5):
            add = get_add(note[i], k)
            dp[i][l][note[i]] = min(dp[i][l][note[i]], dp[i - 1][l][k] + add)

m = inf
for l in range(5):
    for r in range(5):
        m = min(m, dp[n - 1][l][r])
print(m)


# 코멘트 : 결국 인터넷에서 풀이 참고함
