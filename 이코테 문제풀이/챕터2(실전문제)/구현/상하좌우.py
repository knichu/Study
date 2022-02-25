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

# N 입력받기
n = int(input())
x, y = 1, 1
plans = input().split()

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    # 이동 수행
    x, y = nx, ny

print(x, y)


# 코멘트

속도는 내방식이 빠르지만 답안의 코드가 더 깔끔해 보인다. dx, dy로 나누어 각 방향을 -1, 0, 1로 나눈 아이디어는 기억해야겠다.
