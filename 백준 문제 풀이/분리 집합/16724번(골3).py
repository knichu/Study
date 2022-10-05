import sys
input = sys.stdin.readline

def get_direction(s):
    if s == "U":
        return [-1, 0]
    elif s == "R":
        return [0, 1]
    elif s == "D":
        return [1, 0]
    else: # elif s == "L":
        return [0, -1]

def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]

def union(x, y):
    x = find(x)
    y = find(y)
    
    if x > y:
        parents[x] = y
    else:
        parents[y] = x

n, m = map(int, input().split())
grpah = [input().rstrip() for _ in range(n)]
parents = [i for i in range(n * m)]

for i in range(n):
    for j in range(m):
        k = get_direction(grpah[i][j])
        if find(parents[m * i + j]) != find(parents[m * (i + k[0]) + (j + k[1])]):
            union(m * i + j, m * (i + k[0]) + (j + k[1]))
for i in range(n * m):
    find(i)
parents = set(parents)
print(len(parents))


# 코멘트 : 젤 빠른사람 풀이보니 분리집합으로 안함. 다른방법도 
