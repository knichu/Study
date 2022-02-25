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

n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)
    
print(result)



# 코멘트

나는 전체 입력받은 값을 2차원 리스트로 만들어 값들을 처리하려했는데 문제에서는 각 행들 최소값중 최댓값만 찾아서 입력받을때마다 처리했다.
결과는 내방식이 더 빠르게 나왔다. 아직 코딩 배운지 얼마 안되어서 다른이유가 있을수도 있다는 생각을 해본다.
