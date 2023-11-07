import sys
input = sys.stdin.readline

N = int(input().strip())
lst = []
set_lst = set()
for i in range(N):
    x = int(input().strip())
    lst.append(x)
    set_lst.add(x)

ans = 1
for set_lst_idx in set_lst:
    cnt = 1
    start = 0
    # 선택된 i 가 lst[0] 와 같을시, start 위치 조정
    if lst[start] == set_lst_idx:
        k = set_lst_idx
        idx = 0
        while lst[idx] == k:
            idx += 1
        start = idx
        ans = max(start, ans)

    compare_idx = 1
    for j in range(start + 1, N):
        if lst[j] != set_lst_idx:

            if lst[j - compare_idx] == lst[j]:
                cnt += 1
                compare_idx += 1
                ans = max(cnt, ans)
            else:
                cnt = 1
                compare_idx = 1

        else:
            compare_idx += 1

print(ans)


# 코멘트 : 오랜만에 해서 그런지 코드가 좀 더러워지고 가독성이 안좋아졌다.
