import sys
input = sys.stdin.readline

n, k = map(int, input().split())
lst = []
for i in range(1, n + 1):
    lst.append(i)
idx = -1
result = ["<"]
while lst:
    idx += k
    while idx >= n:
        idx -= n
    if n != 1:
        result.append(str(lst[idx]) + ", ")
    else:
        result.append(str(lst[idx]))
        break
    del lst[idx]
    idx -= 1
    n -= 1
result.append(">")
print("".join(result))
