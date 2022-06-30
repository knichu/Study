import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = {}
for i in range(n):
    k, v = input().strip().split()
    lst[k] = v
for i in range(m):
    print(lst[input().strip()])
