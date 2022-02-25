# 내가 작성한 코드

loc = input()

dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

lx = ['1', '2', '3', '4', '5', '6', '7', '8']
ly = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

x = lx.index(loc[1])
y = ly.index(loc[0])

count = 0

for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx <= 7 and 0 <= ny <= 7:
        count += 1
    else:
        continue

print(count)



# 답안 예시

# 현재 나이트의 위치 입력받기
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]
    # 해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)



# 코멘트

너무 어렵게 생각해서 그런지 좀 오래 걸렸다. 답안에서 a, b, c 등의 문자열을 아스키코드 변환하는 방식이 더 깔끔하고 좋은거 같다.
(속도도 더 빠른거 같다.)(바둑판이 무한히 커진다면 답안대로 해야할듯하다.)
