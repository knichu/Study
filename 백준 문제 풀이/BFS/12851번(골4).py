from collections import deque
import sys
input = sys.stdin.readline


def solve(n, k):
    if n >= k:
        print(n - k)
        print(1)
        return

    time = 0
    route_cnt = 0
    lst = [0] * 100001
    found_flag = False
    q = deque()
    q.append((0, n))
    while q:
        cur_time, position = q.popleft()
        if found_flag:
            if cur_time == time and position == k:
                route_cnt += 1

        else:  # elif not found_flag:
            if position == k:
                found_flag = True
                time = cur_time
                route_cnt += 1
            else:  # elif position != k:
                if position * 2 <= 100000:
                    if not lst[position * 2] or lst[position * 2] - 1 == cur_time:
                        q.append((cur_time + 1, position * 2))
                        lst[position * 2] = cur_time + 1
                if position + 1 <= 100000:
                    if not lst[position + 1] or lst[position + 1] - 1 == cur_time:
                        q.append((cur_time + 1, position + 1))
                        lst[position + 1] = cur_time + 1
                if 0 <= position - 1 <= 100000:
                    if not lst[position - 1] or lst[position - 1] - 1 == cur_time:
                        q.append((cur_time + 1, position - 1))
                        lst[position - 1] = cur_time + 1

    print(time)
    print(route_cnt)
    return


N, K = map(int, input().split())
solve(N, K)


# 코멘트 : 쫌만 잘 생각했으면 한번 헤메지 않았을듯 하다.
