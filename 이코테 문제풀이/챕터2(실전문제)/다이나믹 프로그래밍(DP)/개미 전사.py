# 내가 작성한 코드

n = int(input())

rice = list(map(int, input().split()))

d = [0] * 100

d[0] = rice[0]
d[1] = max(rice[0], rice[1]) 
for i in range(2, n):
    d[i] = max(d[i - 1], d[i - 2] + rice[i])

print(d[n - 1])



# 답안 예시
# 정수 N을 입력 받기
n = int(input())
# 모든 식량 정보 입력 받기
array = list(map(int, input().split()))

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 100

# 다이나믹 프로그래밍(Dynamic Programming) 진행 (보텀업)
d[0] = array[0]
d[1] = max(array[0], array[1]) 
for i in range(2, n):
    d[i] = max(d[i - 1], d[i - 2] + array[i])

# 계산된 결과 출력
print(d[n - 1])



# 코멘트

점화식 생각하는데에 너무 오래 걸렸다. 한번 잘못 생각하니까 오류를 발견하기 힘들었다.
