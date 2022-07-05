import sys
input = sys.stdin.readline
import heapq

n = int(input())
q = []
for _ in range(n):
    a = int(input())
    if a == 0:
        if q:
            print(-q[0])
            heapq.heappop(q)
        else:
            print(0)
    else:
        heapq.heappush(q, -a)
