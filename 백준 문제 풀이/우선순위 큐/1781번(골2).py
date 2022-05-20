import heapq
import sys
input = sys.stdin.readline
n = int(input())
idx = [i for i in range(n + 1)]
grp = []
for i in range(n):
    a, b = map(int, input().split())
    grp.append((a, b))
grp.sort()
q = []
for i in range(n):
    a, b = grp[i]
    heapq.heappush(q, b)
    if a < len(q):
        heapq.heappop(q)
print(sum(q))
