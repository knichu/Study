# 내가 작성한 코드

n, m = map(int, input().split())

coin = []
for i in range(n):
    coin.append(int(input()))

d = [0] * (m + 1)

for i in range(1, m + 1):
    for j in coin:
        if i - j == 0:
            d[i] = 1
        if i - j > 0:
            if d[i - j] == 0:
                continue
            if d[i] == 0:
                d[i] = d[i - j] + 1
                continue
            d[i] = min(d[i], d[i - j] + 1)
        if i - j < 0:
            continue
        
if d[m] == 0:
    print(-1)
else:
    print(d[m])



# 답안 예시
# 정수 N, M을 입력 받기
n, m = map(int, input().split())
# N개의 화폐 단위 정보를 입력 받기
array = []
for i in range(n):
    array.append(int(input()))

# 한 번 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [10001] * (m + 1)

# 다이나믹 프로그래밍(Dynamic Programming) 진행(보텀업)
d[0] = 0
for i in range(n):
    for j in range(array[i], m + 1):
        if d[j - array[i]] != 10001: # (i - k)원을 만드는 방법이 존재하는 경우
            d[j] = min(d[j], d[j - array[i]] + 1)

# 계산된 결과 출력
if d[m] == 10001: # 최종적으로 M원을 만드는 방법이 없는 경우
    print(-1)
else:
    print(d[m])
    
    

# 코멘트

이 문제 답안을 보고 여러 테크닉을 배워간다. 아직도 너무 코드가 난잡하다.
