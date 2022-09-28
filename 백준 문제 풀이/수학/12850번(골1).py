# https://www.acmicpc.net/problem/12850

import sys
input = sys.stdin.readline

def dfs(n):
    if dp[dp_idx[n]]:
        return dp[dp_idx[n]]

    if n % 2 == 0:
        dp[dp_idx[n]] = matrix_x(dfs(n // 2), dfs(n // 2))
    else:
        dp[dp_idx[n]] = matrix_x(matrix_x(dfs(n // 2), dfs(n // 2)), dp[1])
    return dp[dp_idx[n]]
    
def matrix_x(graph_1, graph_2):
    graph = [[] for _ in range(8)]
    for i in range(8):
        for j in range(8):
            k = 0
            for x in range(8):
                k += graph_1[i][x] * graph_2[x][j]
            k %= 1000000007
            graph[i].append(k)
    return graph
    
n = int(input())
graph = [
        [0, 1, 1, 0, 0, 0, 0, 0],
        [1, 0, 1, 1, 0, 0, 0, 0],
        [1, 1, 0, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 1, 0, 0],
        [0, 0, 1, 1, 0, 1, 1, 0],
        [0, 0, 0, 1, 1, 0, 0, 1],
        [0, 0, 0, 0, 1, 0, 0, 1],
        [0, 0, 0, 0, 0, 1, 1, 0]
]
dp_idx = dict()
com = []
k = n
while k != 1:
    if k % 2 == 0:
        com.append(k)
    else:
        com.append(k)
        com.append(k // 2 + 1)
    k //= 2
com.append(1)
dp = [[] for _ in range(len(com) + 1)]
dp[1] = graph
for i in range(1, len(com) + 1):
    dp_idx[com[-i]] = i

dfs(n)
print(dp[-1][0][0] % 1000000007)
