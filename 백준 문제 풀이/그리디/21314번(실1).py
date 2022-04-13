import sys

k = sys.stdin.readline()
n = len(k) - 1
max_result = []
min_result = []

num = 0
count = 0
for i in range(n):
    if k[i] == 'K':
        num = (10 ** count) * 5
        max_result.append(str(num))
        count = 0
    else:
        count += 1
for i in range(count):
    max_result.append('1')
max = "".join(max_result)
max = int(max)
print(max)

count = 0
for i in range(n):
    if k[i] == 'K':
        if count > 0:
            min_result.append(str(10 ** (count - 1)))
        min_result.append("5")
        count = 0
    else:
        count += 1
for i in range(count):
    min_result.append('1')
if count > 1:
    for i in range(count - 1):
        min_result.pop()
    for i in range(count - 1):
        min_result.append('0')
min = "".join(min_result)
min = int(min)
print(min)



# 코멘트 : 이런식으로 하면 안될꺼 같다. 각 유형 브론즈부터 풀고 와야겟다
