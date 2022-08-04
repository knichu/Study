import sys
input = sys.stdin.readline
from collections import Counter

n = int(input())
avg = 0
arr = []
for i in range(n):
    num = int(input())
    avg += num
    arr.append(num)
arr.sort()
lst = Counter(arr).most_common()

if n > 1:
    if lst[0][1] == lst[1][1]:
        res = lst[1][0]
    else:
        res = lst[0][0]
else:
    res = lst[0][0]

print(round(avg / n))
print(arr[n // 2])
print(res)
print(arr[-1] - arr[0])
