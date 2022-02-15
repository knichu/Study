# 내가 작성한 코드

n = int(input())

count = 0

for i in range(24):
    for j in range(60):
        for k in range(60):
            if n >= 10:
                if i == n or j == n or k == n:
                    count += 1
                else:
                    continue
                
            else:
                c = list(map(int, str(i) + str(j) + str(k)))
                if c.count(n) >= 1:
                    count += 1
                
                
print(count)



# 답안 예시

h = int(input())

count = 0
for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)



# 코멘트

문제를 잘못이해했거나 문제를 잘못낸듯....말이 너무 애매함
