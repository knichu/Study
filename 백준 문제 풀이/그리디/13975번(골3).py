import sys
import heapq
input = sys.stdin.readline

def combine_file(chap_n, size):
    heapq.heapify(size)
    sum = 0
    for i in range(chap_n - 1):
        a = heapq.heappop(size)
        b = heapq.heappop(size)
        s = a + b
        sum += s
        heapq.heappush(size, s)
    return print(sum)

n = int(input())
for i in range(n):
    chap_n = int(input())
    size = list(map(int, input().split()))
    combine_file(chap_n, size)
