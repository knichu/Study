import sys
input = sys.stdin.readline

while True:
    stc = input().rstrip()
    if stc == ".":
        break
    stack = [0]
    for i in stc:
        if i == "[":
            stack.append(1)
        elif i == "(":
            stack.append(2)
        elif i == "]":
            if stack[-1] == 1:
                stack.pop()
            else:
                print("no")
                break
        elif i == ")":
            if stack[-1] == 2:
                stack.pop()
            else:
                print("no")
                break
    else:
        if len(stack) == 1:
            print("yes")
        else:
            print("no")
