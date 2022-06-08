import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    m, n, x, y = map(int, input().split())
    while x <= n * m:
        if (x - y) % n == 0:
            print(x)
            break
        x += m
    else:
        print(-1)
