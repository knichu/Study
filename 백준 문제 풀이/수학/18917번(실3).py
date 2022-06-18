import sys
input = sys.stdin.readline

n = int(input())
sum = 0
xor = 0
for _ in range(n):
    case = list(map(int, input().split()))
    if case[0] == 1:
        sum += case[1]
        xor ^= case[1]
    elif case[0] == 2:
        sum -= case[1]
        xor ^= case[1]
    elif case[0] == 3:
        print(sum)
    else:
        print(xor)
