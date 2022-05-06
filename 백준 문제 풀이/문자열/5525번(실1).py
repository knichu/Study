import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
s = input().strip()
count = 0
i = 0
for k in range(m):
    if s[k] == "I":
        i = k
        break
i_n = 0

while i < (m - 2):
    if s[i:i + 3] == "IOI":
        if i_n < n - 1:
            i_n += 1
            i += 2
        else:
            i += 2
            count += 1
    else:
        i += 1
        i_n = 0

print(count)
