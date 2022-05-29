import sys
input = sys.stdin.readline
import heapq

q = []
for _ in range(int(input())):
    a = int(input())
    if a == 0:
        if not q:
            print(0)
            continue
        else:
            b = heapq.heappop(q)
            print(b)
            continue
    else:
        heapq.heappush(q, a)
