from collections import deque
import sys
input = sys.stdin.readline
    
def solution(a, b):
    q = deque()
    q.append((a, ""))
    visited = [False] * 10000
    while q:
        a, m = q.popleft()
        if a == b:
            return print(m)
        
        d = (a * 2) % 10000
        if not visited[d]:
            q.append((d, m + "D"))
            visited[d] = True
            
        s = (a + 9999) % 10000
        if not visited[s]:
            q.append((s, m + "S"))
            visited[s] = True
        
        l = (a % 1000) * 10 + a // 1000
        if not visited[l]:
            q.append((l, m + "L"))
            visited[l] = True
        
        r = (a % 10) * 1000 + a // 10
        if not visited[r]:
            q.append((r, m + "R"))
            visited[r] = True

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    solution(a, b)
