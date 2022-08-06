# line 12 의 테크닉 인지하기

import sys
input = sys.stdin.readline

n = int(input())
m = 1
if m > 18:
    m = n - len(str(n)) * 9 - 1
result = 0
for i in range(m, n + 1):
    a = list(map(int, str(i)))  
    s = i + sum(a)
    if n == s:
        result = i
        break
print(result)
