n = int(input())  # n = 5

graph = [[] for i in range(n + 1)]

time = [0] * (n + 1)

for i in range(1, n + 1):
    k = list(map(int, input().split()))
    time[i] = k[0]
    l = len(k)
    for j in range(1, l-1):
        graph[i].append(k[j])  

# graph = [[]
#          []
#          [1]
#          [1]
#          [1, 3]
#          [3]
# ]

# time = [0, 10, 10, 4, 4, 3]

result_time = 0
current_time = 0

def dfs(graph, start):
    current_time += time[start]
    a = current_time
    for i in graph[start]:
        current_time = a
        if not graph[start]:
            result_time = max(result_time, current_time)
        else:
            dfs(graph, i)

    print(result_time)
    current_time = 0
    result_time = 0

for i in range(n):
    dfs(graph, i)
