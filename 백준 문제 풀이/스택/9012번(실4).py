import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    string = input().rstrip()
    stack = []
    f = True
    for i in string:
        if i == "(":
            stack.append(1)
        else:
            if stack:
                stack.pop()
            else:
                f = False
                break
    if f:
        if stack:
            print("NO")
        else:
            print("YES")
    else:
        print("NO")        
