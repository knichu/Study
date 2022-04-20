import sys
input = sys.stdin.readline

def combine_file(chap_n, size):
    size.sort()
    dp = [0] * 500
    dp[0] = size[0] + size[1]
    rem = dp[0]
    b = size[2]
    for i in range(1, chap_n - 2):
        if rem <= size[i + 2]:
            a = rem + b
            dp[i] = dp[i - 1] + a
            rem = a
            b = size[i + 2] 
        elif rem > size[i + 2]:
            b = b + size[i + 2]
            dp[i] = dp[i - 1] + b
    dp[chap_n - 2] = dp[chap_n - 3] + b + rem
    print(dp[chap_n - 2])
    
n = int(input())
for i in range(n):
    chap_n = int(input())
    size = list(map(int, input().split()))
    combine_file(chap_n, size)
