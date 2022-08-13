import sys
input = sys.stdin.readline

target = input().strip()
bomb = input().strip()
lbomb = list(bomb)
stack = []
n, m = len(target), len(bomb)
if n >= m:
    for i in range(n):
        if len(stack) < (m - 1):
            stack.append(target[i])
        else:
            stack.append(target[i])
            if stack[-m:] == lbomb:
                del stack[-m:]
    print(''.join(stack) if stack else "FRULA")
else:
    print(target)
