import sys
input = sys.stdin.readline

n, k = map(int, input().split())
s = list(map(int, list(input().rstrip())))

idx = 0
mx = 0
for i in range(k + 1):
    if mx < s[i]:
        mx = s[i]
        idx = i
stack = []
for i in range(idx, n):
    if len(stack) + k - i == 0:
        for j in range(i, n):
            stack.append(s[j])
        break

    if not stack:
        stack.append(s[i])
    elif s[i] <= stack[-1]:
        stack.append(s[i])
    else:
        for _ in range(len(stack)):
            if stack[-1] < s[i]:
                stack.pop()
                if len(stack) + k - i == 0:
                    break
            else:
                break
        stack.append(s[i])
        
while len(stack) > (n - k):
    stack.pop()
stack = list(map(str, stack))
print("".join(stack))
