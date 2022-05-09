import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    global cost
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if cost[a - 1] < cost[b - 1]:
        parent[b] = a
    else:
        parent[a] = b
        
# 학생 수 N, 친구관계 수 M, 가지고 있는 돈 k 
n, m, k = map(int, input().split())
cost = list(map(int, input().split()))
parent = [i for i in range(n + 1)]
    
for i in range(m):
    a, b = map(int, input().split())
    union_parent(parent, a, b)
    
for i in range(1, n + 1):
    find_parent(parent, i)

new_parent = [0]
for i in parent:
    if i not in new_parent:
        new_parent.append(i)

parent_sum = 0
for i in range(1, len(new_parent)):
    parent_sum += cost[new_parent[i] - 1]

if parent_sum <= k:
    print(parent_sum)
else:
    print("Oh no")
