import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coin_list = []
for _ in range(n):
    coin_list.append(int(input()))
cnt = 0
for i in range(n - 1, -1, -1):
    if coin_list[i] <= k:
        a = k // coin_list[i]
        cnt += a
        k -= a * coin_list[i]
print(cnt)
