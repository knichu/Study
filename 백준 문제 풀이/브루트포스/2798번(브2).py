import sys
input = sys.stdin.readline
from itertools import combinations

n, m = map(int, input().split())
lst = list(map(int, input().split()))
k = list(combinations(lst, 3))
res = []
for a, b, c in k:
    s = a + b + c
    if s < m:
        res.append(s)
    elif s == m:
        res.append(s)
        break
res.sort()
print(res[-1])
