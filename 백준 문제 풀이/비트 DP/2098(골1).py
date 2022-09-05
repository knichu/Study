import sys
input = sys.stdin.readline

def tsp(n, dists):
    VISITED_ALL = (1 << n) - 1
    cache = [[None] * (1 << n) for _ in range(n)]
    INF = float('inf')
    
    def find_path(last, visited):
        if visited == VISITED_ALL:
            return dists[last][0] or INF

        if cache[last][visited] is not None:
            return cache[last][visited]
            
        tmp = INF
        for city in range(n):
            # 방문하지 않은 도시고  and  현재도시(last)로 부터 다음도시(city)까지 길이 있다면
            if visited & (1 << city) == 0 and dists[last][city] != 0:
                tmp = min(tmp, find_path(city, visited | (1 << city)) + dists[last][city])
        cache[last][visited] = tmp
        return tmp
    
    return find_path(0, 1 << 0)

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
print(tsp(n, graph))
