n = int(input())
time = list(map(int, input().split()))
time.sort()
delay_time = [0] * n
delay_time[0] = time[0]
total_time = 0

for i in range(1, n):
    delay_time[i] = delay_time[i - 1] + time[i]

for i in range(n):
    total_time += delay_time[i]

print(total_time)
