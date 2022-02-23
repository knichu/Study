# 내가 작성한 코드(미완)

# x = (array[0] + array[1] + ... array[n] - m) / n
#                                           12  3

def cut(array, num, length):
    if num == 1:
        return array[0] - length
    
    for i in range(1, num):
        x = array[i] - array[i - 1]
        if x >= length:
            return array[0] - length
        elif :
            





n, m = map(int, input().split())

tteok = list(map(int, input().split()))

tteok.sort()
