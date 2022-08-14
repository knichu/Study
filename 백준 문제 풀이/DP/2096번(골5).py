import sys
input = sys.stdin.readline

n = int(input())
maxdp = [[0] * 3 for _ in range(2)]
mindp = [[0] * 3 for _ in range(2)]
for i in range(n):
    ck = i % 2
    graph = list(map(int, input().split()))
    maxdp[ck][0] = graph[0] + max(maxdp[ck - 1][0], maxdp[ck - 1][1])
    maxdp[ck][1] = graph[1] + max(maxdp[ck - 1][0], maxdp[ck - 1][1], maxdp[ck - 1][2])
    maxdp[ck][2] = graph[2] + max(maxdp[ck - 1][1], maxdp[ck - 1][2])
    mindp[ck][0] = graph[0] + min(mindp[ck - 1][0], mindp[ck - 1][1])
    mindp[ck][1] = graph[1] + min(mindp[ck - 1][0], mindp[ck - 1][1], mindp[ck - 1][2])
    mindp[ck][2] = graph[2] + min(mindp[ck - 1][1], mindp[ck - 1][2])
print(max(maxdp[ck]), min(mindp[ck]))
