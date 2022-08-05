import sys
input = sys.stdin.readline
from collections import Counter

test_case = int(input())
for _ in range(test_case):
    n, m = map(int, input().split())
    lst = list(map(int, input().split()))
    ck = lst[m]
    visited = [False] * n
    counting = Counter(lst).most_common()
    counting.sort(reverse = True)
    counting_idx = counting[0][0]
    counting_num = counting[0][1]
    k = 0
    num = 0
    idx = 0
    result = 0
    while True:
        if idx == n:
            idx = 0
        if not visited[idx]:
            if lst[idx] == counting_idx:
                visited[idx] = True
                result += 1
                num += 1
                if m == idx:
                    break
                if num == counting_num:
                    k += 1
                    counting_idx = counting[k][0]
                    counting_num = counting[k][1]
                    num = 0
        idx += 1
    print(result)
