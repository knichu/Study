import re

a = input()
a = re.split('([-+])', a)
b = len(a)
for i in range(b):
    if a[i] == '-':
        continue
    elif a[i] == '+':
        continue
    else:
        a[i] = int(a[i])

total = 0
for i in range(b):
    if a[i] == '-':
        for j in range(i, b):
            if a[j] == '+':
                continue
            elif a[j] == '-':
                continue
            else:
                total = total - a[j]
        break
    elif a[i] == '+':
        continue
    else:
        total = total + a[i]

print(total)



# 코멘트 : 너무 코드가 난잡하다. 다른사람의 코드를 보면 안 이럴꺼 같다.
