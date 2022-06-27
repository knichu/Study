import sys
input = sys.stdin.readline

while True:
    lst = list(map(int, input().split()))
    if lst[0] == 0:
        break
    stack = []
    mx = 0
    for i in range(1, lst[0] + 1):
        x = lst[i]
        if not stack:
            stack.append((x, 1))
        elif x > stack[-1][0]:
            stack.append((x, 1))
        elif x == stack[-1][0]:
            a, b = stack.pop()
            stack.append((a, b + 1))
        else:
            cnt = 0
            while x < stack[-1][0]:
                a, b = stack.pop()
                mx = max(mx, a * (b + cnt))
                cnt += b
                if not stack:
                    break
            stack.append((x, 1 + cnt))
    cnt = 0
    while stack:
        a, b = stack.pop()
        mx = max(mx, a * (b + cnt))
        cnt += b
    print(mx)
