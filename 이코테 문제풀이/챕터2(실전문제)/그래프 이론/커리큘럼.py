# 내가 작성한 코드(임시)

from collections import deque

n = int(input())

indegree = [0] * (n + 1)

graph = [[] for i in range(n + 1)]

time = [] * (n + 1)

for i in range(1, n + 1):
    k = list(map(int, input().split()))
    time[i] = k[0]
    l = len(k)
    for j in range(1, l-1):
        graph[k[j]].append(i)
        indegree[i] += 1      # deque 이용해서 leftpop을 활용해야 할거 같은데 방법을 모르겠음.

# graph  = [[]
#           [2, 3, 4]
#           []
#           [4, 5]
#           []
#           []
# ]

# 위상 정렬 함수
def topology_sort():
    result = [] # 알고리즘 수행 결과를 담을 리스트
    q = deque() # 큐 기능을 위한 deque 라이브러리 사용

    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    # 큐가 빌 때까지 반복
    while q:
        # 큐에서 원소 꺼내기
        now = q.popleft()
        result.append(now)
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]:
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)

topology_sort()  # result = [1, 2, 3, 4, 5]

for i in range(n):
    
    
