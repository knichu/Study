import heapq
import sys
input = sys.stdin.readline

n = int(input())
n_list = []
for i in range(n):
    n_list.append(int(input()))
q = []

for i in range(n):
    k = n_list[i]
    if k > 0:
        heapq.heappush(q, (k, 1))
    elif k < 0:
        heapq.heappush(q, (-k, -1))
    elif k == 0:
        if len(q) > 0:
            a, b = heapq.heappop(q)
            if b == 1:
                print(a)
            elif b == -1:
                print(-a)
        else:
            print(0)
