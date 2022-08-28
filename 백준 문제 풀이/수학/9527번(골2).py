import sys
input = sys.stdin.readline

def div(k, i):
    a , b = k // (2 ** i), k % (2 ** i)
    if (a % 2) == 1:
        return (a // 2) * (2 ** i) + (b + 1)
    else:
        return (a // 2) * (2 ** i)
x, y = map(int, input().split())
i = 0
y_cnt = 0
while (y // (2 ** i)) != 0:
    y_cnt += div(y, i)
    i += 1
i = 0
x_cnt = 0
while ((x - 1) // (2 ** i)) != 0:
    x_cnt += div(x - 1, i)
    i += 1
print(y_cnt - x_cnt)
