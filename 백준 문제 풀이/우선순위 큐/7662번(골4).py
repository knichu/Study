import sys
input = sys.stdin.readline
import heapq

t = int(input())
for _ in range(t):
    k = int(input())
    visited = [False] * k
    low_q, high_q = [], []
    for i in range(k):
        op, n = input().rstrip().split()
        n = int(n)
        if op == "I":
            heapq.heappush(low_q, (n, i))
            heapq.heappush(high_q, (-n, i))
            visited[i] = True
        elif n == 1:
            while high_q and not visited[high_q[0][1]]:
                heapq.heappop(high_q)
            if high_q:
                visited[high_q[0][1]] = False
                heapq.heappop(high_q)
        else:
            while low_q and not visited[low_q[0][1]]:
                heapq.heappop(low_q)
            if low_q:
                visited[low_q[0][1]] = False
                heapq.heappop(low_q)
    while high_q and not visited[high_q[0][1]]:
        heapq.heappop(high_q)
    while low_q and not visited[low_q[0][1]]:
        heapq.heappop(low_q)
    if high_q and low_q:
        print(-high_q[0][0], low_q[0][0])
    else:
        print('EMPTY')
