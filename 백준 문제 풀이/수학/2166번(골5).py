import sys
input = sys.stdin.readline

n = int(input())
lst = []
for i in range(n):
    x, y = map(int, input().split())
    lst.append((x, y))
lst.append(lst[0])
s = 0
for i in range(n):
    s = s + lst[i][0] * lst[i + 1][1] - lst[i][1] * lst[i + 1][0]
print(abs(round((s / 2), 1)))
