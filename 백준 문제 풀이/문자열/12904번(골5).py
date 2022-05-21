import sys
input = sys.stdin.readline
from collections import deque

s = input().strip()
t = input().strip()

q = deque()
q.append(t)
while q:
    a = q.popleft()
    
    if a[-1] == "A":
        q.append(a[:-1])
    else: # elif a[-1] == "B":
        q.append(a[-2::-1])
    if a == s:
        print(1)
        break
    if len(a) <= len(s):
        print(0)
        break
