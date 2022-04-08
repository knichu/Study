# 내가 작성한 코드

from collections import deque

n = int(input())

k = list(map(int, input().split()))
k.sort(reverse = True)
k = deque(k)

result = 0

while k:
    a = k[0]
    if a <= n:
        for i in range(a):
            k.popleft()
        result += 1
        n = n - a
    else:
        break
    
print(result)



