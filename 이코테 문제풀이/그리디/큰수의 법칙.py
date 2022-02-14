# 내가 작성한 코드

n, m, k = map(int, input().split())

c = list(map(int, input().split()))

c.sort(reverse=True)

a, b = divmod(m, k+1)

sum = ((c[0] * k) + c[1])*a + c[0]*b

print(sum)



# 답안 예시

n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

count = int(m / (k + 1)) * k
count += m % (k + 1)

result = 0
result += (count) * first
result += (m - count) * second

print(result)



# 코멘트

sort(reverse = True) 해서 앞에 두개를 따오기 보단 sort() 해서 맨뒤 2개를 따오자.  
속도에서 유의미한 차이가 난다.  
