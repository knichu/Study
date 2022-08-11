import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = list(map(int, input().split()))
start, end = 1, max(lst)
while start <= end:
    idx = (start + end) // 2
    s = 0
    for i in lst:
        if i >= idx:
            s += i - idx
    if s >= m:
        start = idx + 1
    else: # elif s < m:
        end = idx - 1
print(end)

# 코멘트 : pypy로 통과함
