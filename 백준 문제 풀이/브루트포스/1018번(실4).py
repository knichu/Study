import sys
input = sys.stdin.readline

def solution(x ,y):
    ck = [0, "B", "W"]
    idx = 1
    result = 0
    for i in range(x, x + 8):
        for j in range(y, y + 8):
            if lst[i][j] != ck[idx]:
                result += 1
            if j != (y + 7):
                idx = -idx
    result = min(result, 64 - result)
    return result

n, m = map(int, input().split())
lst = [input().strip() for _ in range(n)]
a = 32
for i in range(n - 7):
    for j in range(m - 7):
        a = min(solution(i, j) , a)
print(a)
