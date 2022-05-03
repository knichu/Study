import sys
input = sys.stdin.readline

let = list(input().strip())
n = len(let)

def solution(let, n):
    ck = "Z"
    dp = [[0] * n for i in range(n)]
    used = [0] * n
    result = [""] * n
    cas_result = [""] * n
    for i in range(n):
        dp[0][i] = let[i]
    for i in range(n - 1, -1, -1):
        if dp[0][i] <= ck:
            ck = dp[0][i]
            ck_i = i
    used[ck_i] = 1
    result[ck_i] = let[ck_i]
    cas_result[ck_i] = let[ck_i]
    a = "".join(result)
    print(a)
    
    for i in range(1, n):
        for j in range(n):
            if used[j] == 0:
                cas_result[j] = let[j]
                a = "".join(cas_result)
                dp[i][j] = a
                cas_result[j] = ""
                
        loc = comparing(dp[i], n, i + 1)
        print(dp[i][loc])

        used[loc] = 1
        result[loc] = let[loc]
        cas_result[loc] = let[loc]
    return 

def comparing(list, n, l):
    visited = [0] * n
    for i in range(n):
        if list[i] == 0:
            visited[i] = 1
    count = []
    
    for i in range(l):
        if len(count) == 1:
            return count[0]
        count = []
        cek = "Z"
        
        for j in range(n):
            if list[j] != 0:
                if visited[j] == 0:
                    k = list[j][i]
                    if k <= cek:
                        cek = k
                    
        for j in range(n):
            if list[j] != 0:
                if visited[j] == 0:
                    if list[j][i] == cek:
                        count.append(j)
                    elif list[j][i] != cek:
                        visited[j] = 1
    return count[0]
                
solution(let, n)
