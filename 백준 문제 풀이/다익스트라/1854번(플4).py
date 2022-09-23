import sys
input = sys.stdin.readline
import heapq

n, m, k = map(int, input().split())
distance = [[] for _ in range(n + 1)]
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra():
    q = []
    heapq.heappush(q, (0, 1))
    distance[1].append(0)
    while q:
        dist, node = heapq.heappop(q)

        for next in graph[node]:
            cost = dist + next[1]
            
            if len(distance[next[0]]) == k:
                if distance[next[0]][0] < (-cost):
                    heapq.heappop(distance[next[0]])
                    heapq.heappush(distance[next[0]], -cost)
                    heapq.heappush(q, (cost, next[0]))
            else:
                heapq.heappush(distance[next[0]], -cost)
                heapq.heappush(q, (cost, next[0]))
   
dijkstra()

if len(distance[1]) < k:
    print(-1)
else:
    print(-distance[1][0])
for i in range(2, n + 1):
    if len(distance[i]) < k:
        print(-1)
    else:
        print(-distance[i][0])
