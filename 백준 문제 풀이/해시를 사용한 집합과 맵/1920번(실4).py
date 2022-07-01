import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
lst = set()
for i in range(n):
    lst.add(num[i])
m = int(input())
ck = list(map(int, input().split()))
for i in range(m):
    if ck[i] in lst:
        print(1)
    else:
        print(0)
