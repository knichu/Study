import sys
input = sys.stdin.readline

n = int(input())
rope = []
m = 0

for i in range(n):
    rope.append(int(input()))

rope.sort()

for i in range(n):
    m = max(rope[i] * (n - i), m)

print(m)
