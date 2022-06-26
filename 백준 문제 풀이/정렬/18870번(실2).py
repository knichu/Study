import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
sort_lst = []
for i in range(n):
    sort_lst.append((lst[i], i))
sort_lst.sort()
result_lst = [0] * n
cnt = 0
idx = 0
while idx < n:
    result_lst[sort_lst[idx][1]] = cnt
    if idx == (n - 1):
        break
    while sort_lst[idx][0] == sort_lst[idx + 1][0]:
        idx += 1
        result_lst[sort_lst[idx][1]] = cnt
        if idx == (n - 1):
            break
    if idx == (n - 1):
        break
    idx += 1
    cnt += 1

for i in range(n):
    print(result_lst[i], end = ' ')
