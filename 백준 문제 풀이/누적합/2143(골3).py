import sys
input = sys.stdin.readline
from bisect import bisect_left, bisect_right

t = int(input())
n = int(input())
nlst = list(map(int, input().split()))
m = int(input())
mlst = list(map(int, input().split()))

ndp = []
for i in range(n):
    ndp.append(nlst[i])
    for j in range(i + 1, n):
        ndp.append(ndp[-1] + nlst[j])
ndp.sort()

mdp = []
for i in range(m):
    mdp.append(mlst[i])
    for j in range(i + 1, m):
        mdp.append(mdp[-1] + mlst[j])
mdp.sort()

result = 0
for i in ndp:
    k = t - i
    a = bisect_left(mdp, k)
    b = bisect_right(mdp, k)
    result += b - a
print(result)
