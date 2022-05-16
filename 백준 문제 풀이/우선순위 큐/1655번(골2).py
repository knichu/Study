import heapq
import sys
input = sys.stdin.readline

low_q = []
high_q = []

n = int(input())
mid = int(input())
print(mid)
state = True
cnt = 0

for _ in range(n - 1):
    a = int(input())
    
    if a <= mid:
        if state == True:
            heapq.heappush(high_q, mid)
            if low_q == []:
                mid = a
                print(mid)
                state = False
            else:
                if (- low_q[0]) >= a:
                    mid = - heapq.heappop(low_q)
                    heapq.heappush(low_q, - a)
                    print(mid)
                    state = False
                else: # (- low_q[0]) < a:
                    mid = a
                    print(mid)
                    state = False
        else: # if state == False:
            heapq.heappush(low_q, - a)
            print(mid)
            state = True
        
    else: # elif a > mid:
        if state == True:
            heapq.heappush(high_q, a)
            print(mid)
            state = False
        else: # if state == False:
            heapq.heappush(low_q, - mid)
            if high_q[0] < a:
                mid = heapq.heappop(high_q)
                heapq.heappush(high_q, a)
                print(mid)
                state = True
            else: # high_q[0] >= a:
                mid = a
                print(mid)
                state = True
                
                
# 코멘트 : len의 시간복잡도 1인점과 mid값을 low_q에 포함시켰으면 더 간결할수 있었다...
