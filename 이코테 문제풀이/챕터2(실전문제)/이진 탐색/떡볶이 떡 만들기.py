# 내가 작성한 코드

def cut(array, num, length):
    if num == 1:
        return array[0] - length
    
    k = array[0]
    for i in range(1, num - 1):
        k = k + array[i]
        x = (k - length) // (i + 1)
        if x >= array[i + 1]:
            return x
        
    k = k + array[num - 1]
    x = (k - length) // (i + 1)
    return x
    

n, m = map(int, input().split())

tteok = list(map(int, input().split()))

tteok.sort(reverse = True)

print(cut(tteok, n, m))




# 답안 예시

# 떡의 개수(N)와 요청한 떡의 길이(M)을 입력
n, m = list(map(int, input().split(' ')))
# 각 떡의 개별 높이 정보를 입력
array = list(map(int, input().split()))

# 이진 탐색을 위한 시작점과 끝점 설정
start = 0
end = max(array)

# 이진 탐색 수행 (반복적)
result = 0
while(start <= end):
    total = 0
    mid = (start + end) // 2
    for x in array:
        # 잘랐을 때의 떡볶이 양 계산
        if x > mid:
            total += x - mid
    # 떡볶이 양이 부족한 경우 더 많이 자르기 (오른쪽 부분 탐색)
    if total < m:
        end = mid - 1
    # 떡볶이 양이 충분한 경우 덜 자르기 (왼쪽 부분 탐색)
    else:
        result = mid # 최대한 덜 잘랐을 때가 정답이므로, 여기에서 result에 기록
        start = mid + 1

# 정답 출력
print(result)



# 코멘트

아직도 문제를 너무 수학적으로 접근하는거 같다. 이 문제도 앞에서 이진탐색이란걸 배웟는데 이진탐색을 어떻게 활용해볼라해도 잘 안되어서 방정식 세워서 해결했다.
좀 더 익숙해져야겟다....

