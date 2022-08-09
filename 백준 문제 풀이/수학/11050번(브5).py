import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a, b = 1, 1
for i in range(k + 1, n + 1):
    a *= i
for i in range(1, n - k + 1):
    b *= i
print(a // b)
