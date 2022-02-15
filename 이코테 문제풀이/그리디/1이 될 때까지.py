# 내가 작성한 코드

n, k = map(int, input().split())

count = 0

while n != 1:
    if n % k != 0:
        n -= 1
        count += 1
    
    else:
        n = n / k
        count += 1

print(count)



# 답안 예시


n, k = map(int, input().split())

result = 0

while True:
    target = (n // k) * k
    result += (n - target)
    n = target
    
    if n < k:
        break
    
    result += 1
    n //= k

result += (n - 1)
print(result)



# 코멘트

파이썬에선 if문을 쓰면 싫어하나..?
