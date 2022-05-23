import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
tree = [[] for i in range(n + 1)]
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    tree[a].append((b, c))
    tree[b].append((a, c))

q = []

for i in range(1, n + 1):
    if len(tree[i]) == 1:
        q.append(i)

def dfs(x, l):
    global length_list
    global tree
    global visited
    if visited[x] == True:
        return

    if len(tree[x]) == 1:
        length_list.append((l, x))
        return

    else:
        visited[x] = True
        for i in tree[x]:
            dfs(i[0], l + i[1])
if n > 1:
    a = q[0]
    visited = [False] * (n + 1)
    visited[a] = True
    next_a = tree[a][0][0]
    length = tree[a][0][1]
    length_list = []

    dfs(next_a, length)

    mx = max(length_list)

    a = mx[1]
    visited = [False] * (n + 1)
    visited[a] = True
    next_a = tree[a][0][0]
    length = tree[a][0][1]
    length_list = []

    dfs(next_a, length)

    print(max(length_list)[0])
else:
    print(0)
