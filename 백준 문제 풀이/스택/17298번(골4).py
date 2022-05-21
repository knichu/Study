import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
result = [-1] * n
stack = [0]

for i in range(n):
    while stack and lst[stack[-1]] < lst[i]:
        a = stack.pop()
        result[a] = lst[i]
    stack.append(i)

print(*result)
