import sys
input = sys.stdin.readline

def solve():
    result = []
    for k in range(1024):
        graph = b_graph[:]
        n = bin(k)[2:]
        for i in range(len(n)):
            if n[-i - 1] == '1':
                change(0, 9 - i, graph)
        cnt = bin(k).count("1")
        for i in range(9):
            n = bin(graph[i])[2:]
            for j in range(len(n)):
                if n[-j - 1] == '1':
                    change(i + 1, 9 - j, graph)
                    cnt += 1
        if graph[9] == 0:
            result.append(cnt)
    if result:
        print(min(result))
    else:
        print(-1)

def change(x, y, graph):
    a, b = 0, 0
    for i in range(3):
        ny = y + dy[i]
        if 0 <= ny < 10:
            a += 2 ** (9 - ny)
    graph[x] ^= a
    if x != 9:
        b += 2 ** (9 - y)
        graph[x + 1] ^=  b    

graph = [input().rstrip() for _ in range(10)]
b_graph = []
for i in range(10):
    k = graph[i]
    count = ""
    for j in range(10):
        if graph[i][j] == "O":
            count += "1"
        else:
            count += "0"
    b_graph.append(int(count, 2))
dy = [-1, 0, 1]
solve()
