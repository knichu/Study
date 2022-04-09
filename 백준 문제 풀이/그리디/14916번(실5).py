import sys

n = int(sys.stdin.readline())

table = [0] * (100001)
table[0] = -1
table[1] = -1
table[2] = 1  
table[3] = -1
table[4] = 2
table[5] = 1

for i in range(1, n + 1):
    if table[i - 5] >= 1:
        table[i] = table[i - 5] + 1
    elif table[i - 2] >= 1:
        table[i] = table[i - 2] + 1

print(table[n])
