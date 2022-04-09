n = int(input())
tip = []
for i in range(n):
    tip.append(int(input()))
tip.sort(reverse = True)

total_tip = 0

for i in range(n):
    if tip[i] - i < 0:
        break
    else:
        total_tip += tip[i] - i

print(total_tip)
