import sys
input = sys.stdin.readline
from collections import deque
for _ in range(int(input())):
    com = input().strip()
    n = int(input().strip())
    num = input().strip()
    num = num[1:-1].split(',')
    num = deque(num)
    start = 0
    end = n - 1
    state = 1
    flag = True
    for i in com:
        if i == "R":
            start, end = end, start
            state = - state
        else: # elif i == "D":
            if state == 1:
                if start == (end + 1):
                    flag = False
                    break
                else:
                    start += 1
            else:
                if (start + 1) == end:
                    flag = False
                    break
                else:
                    start -= 1
    if flag == True:
        res = ["["]
        for i in range(start, end + state, state):
            res.append(num[i])
            res.append(",")
        if len(res) > 1:
            res.pop()
        res.append("]")
        print(''.join(res))
    else:
        print("error")
