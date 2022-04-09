import sys
input = sys.stdin.readline

n = int(input())
road = list(map(int, input().split()))
oil= list(map(int, input().split()))
visited = oil[0]
time = 0
cost = 0

for i in range(1, n):
    while oil[i] < visited:
        for j in range(time, i):
            cost += visited * road[j]
        time = i
        visited = oil[i]
for k in range(time, n - 1):
    cost += visited * road[k]

print(cost)
