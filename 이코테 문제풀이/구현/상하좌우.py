# 내가 작성한 코드

n = int(input())

map = [[0 for j in range(n + 2)] for i in range(n + 2)]

way = input().split()

x, y = 1, 1

for i in way:
    if i == 'L':
        if y - 1 == 0:
            continue
        y -= 1
        
    elif i == 'R':
        if y + 1 == n + 1:
            continue
        y += 1

    elif i == 'U':
        if x - 1 == 0:
            continue
        x -= 1

    elif i == 'D':
        if x + 1 == 0:
            continue
        x += 1

print(x, y)


# 답안 예시



# 코멘트


