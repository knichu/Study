# 내가 작성한 코드

import time
start = time.time()


n, m, k = map(int, input().split())

c = list(map(int, input().split()))

c.sort(reverse=True)

a, b = divmod(m, k+1)

sum = ((c[0] * k) + c[1])*a + c[0]*b

print(sum)


end = time.time()
print(f"{end - start:.5f} sec")

#

