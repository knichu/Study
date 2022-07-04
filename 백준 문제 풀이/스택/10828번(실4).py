import sys
input = sys.stdin.readline

n = int(input())
stack = []
for _ in range(n):
    com = input().strip()
    if com == "pop":
        if stack:
            a = stack.pop()
            print(a)
        else:
            print(-1)
    elif com == "size":
        print(len(stack))
    elif com == "empty":
        if stack:
            print(0)
        else:
            print(1)
    elif com == "top":
        if stack:
            print(stack[-1])
        else:
            print(-1)
    else:
        com = list(com.split())
        stack.append(com[-1])
