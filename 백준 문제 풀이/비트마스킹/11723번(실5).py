import sys
input = sys.stdin.readline

m = int(input())
lst = [0] * 21
for _ in range(m):
    command = list(map(str, input().strip().split()))
    com = command[0]
    if com == "all":
        lst = [1] * 21
        continue
    elif com == "empty":
        lst = [0] * 21
        continue
    num = int(command[1])
    if com == "add":
        lst[num] = 1
    elif com == "remove":
        lst[num] = 0
    elif com == "check":
        print(lst[num])
    else: #elif com == "toggle":
        if lst[num] == 1:
            lst[num] = 0
        else:
            lst[num] = 1
