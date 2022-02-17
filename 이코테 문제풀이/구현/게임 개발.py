# 내가 작성한 코드

n, m = map(int, input().split())
x, y, d = map(int, input().split())

w = [(0, -1, -1), (-1, 0, 0), (0, 1, 1), (1, 0, 2), (0, -1, 3)]

map = [list(map(int, input().split())) for i in range(n)]
map[x][y] = 2
stay_count = 0
nx = 0
ny = 0

while True:
    for (i, j, k) in w:
        if k + 1 == d:
            nx = x + i
            ny = y + j
            if map[nx][ny] == 1 or map[nx][ny] == 2:
                stay_count += 1
            else:
                x = nx
                y = ny
                map[x][y] = 2
                stay_count = 0
    if d == 0:
        d = 3
    else:
        d -= 1          
    if stay_count >= 4:
        break
    else:
        continue
                
result = 0

for i in range(n):
    for j in range(m):
        if map[i][j] == 2:
            result += 1
        else:
            continue
        
print(result)



# 답안 예시

# N, M을 공백을 기준으로 구분하여 입력받기
n, m = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0] * m for _ in range(n)]
# 현재 캐릭터의 X 좌표, Y 좌표, 방향을 입력받기
x, y, direction = map(int, input().split())
d[x][y] = 1 # 현재 좌표 방문 처리

# 전체 맵 정보를 입력받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 시뮬레이션 시작
count = 1
turn_time = 0
while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있다면 이동하기
        if array[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 바다로 막혀있는 경우
        else:
            break
        turn_time = 0

# 정답 출력
print(count)



# 코멘트

좀 더 깔끔하게 표현하려면 함수를 정의해주는것도 방법이란걸 숙지하자.
