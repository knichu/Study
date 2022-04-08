# 내가 작성한 코드(임시)

# 백준 1787번 KMP문제 정답진행도 2% 컷

n = int(input())
pat = input()

a = pat[0]
sum = 0
p = [0] * n

for i in range(n):
    if pat[i] == a:
        p[i] = i
        sum += p[i]
    else:
        p[i] = p[i - 1]
        sum += p[i - 1]

print(sum)
