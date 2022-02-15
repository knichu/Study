# 내가 작성한 코드

n, m = map(int, input().split())

data = [list(map(int, input().split())) for i in range(n)]

value = 0

for i in range(n):
    if min(data[i]) > value:
        value = min(data[i])
    else:
        continue
    
print(value)



# 답안 예시
생략


# 코멘트

나는 전체 입력받은 값을 2차원 리스트로 만들어 값들을 처리하려했는데 문제에서 각 행들 최소값중 최댓값만 찾으면 되므로 각 행들을 입력받을때마다 처리하는게 처리속도가 빠른듯 하다.
