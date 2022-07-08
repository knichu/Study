import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = list(map(int, input().split()))
sumlst = [0]
for i in range(n):
    sumlst.append(lst[i] + sumlst[-1])
for i in range(m):
    i, j = map(int, input().split())
    print(sumlst[j] - sumlst[i - 1])
