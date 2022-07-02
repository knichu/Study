import math
import sys
input = sys.stdin.readline

a, b, v = map(int, input().split())

if a >= v:
    print(1)
else:
    s = v - a
    print(int(math.ceil(s / (a - b))) + 1)
