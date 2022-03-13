import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())  # n = 6, m = 11

start = int(input())

graph = [[] for i in range(n + 1)]  # [[ ], [ ], [ ], [ ], [ ], [ ], [ ]]

distance = [INF] * (n + 1)  # [INF, INF, INF, INF, INF, INF, INF]

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    
# graph = [ []                       # 0
#           [(2, 2), (3, 5), (4, 1)] # 1
#           [(3, 3), (4, 2)]         # 2
#           [(2, 3), (6, 5)]         # 3
#           [(3, 3), (5, 1)]         # 4
#           [(3, 1), (6, 2)]         # 5
#           []                       # 6
#         ]
    
def dijkstra(start):  # start = 1
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        dist, now = heapq.heappop(q)  # dist = 0, now = 1
        
        if distance[now] < dist:
            continue
        
        for i in graph[now]:
            cost = dist + i[1]  # cost = 0 + 2
            if cost < distance[i[0]]:  # 2 < INF
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))  # (거리 2, 노드 2) 큐에 삽입
    
dijkstra(start)

for i in range(1, n + 1):
    print(distance[i])
