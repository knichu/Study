import sys
input = sys.stdin.readline
n = int(input())
time = []
for i in range(n):
    time.append(list(map(int, input().split())))
time.sort(key = lambda x : (x[1], x[0]))
cnt = 1
end = time[0][1]
for i in range(1, n):
    if time[i][0] >= end:
        end = time[i][1]
        cnt += 1
print(cnt)
