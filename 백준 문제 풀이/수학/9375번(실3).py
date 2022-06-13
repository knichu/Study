import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    types = {}
    for _ in range(n):
        cloth, type = map(str, input().split())
        if type not in types:
            types[type] = 1
        else:
            types[type] += 1
    if types:
        result = 1
        for i in types:
            result *= (types[i] + 1)
        print(result - 1)
    else:
        print(0)
