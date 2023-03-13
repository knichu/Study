def solution(cap, n, deliveries, pickups):
    deli_index, pick_index = 0, 0
    deli_move_list, pick_move_list = [], []
    deli_move_remain, pick_move_remain = cap, cap

    for i in range(n - 1, -1, -1):
        if deliveries[i] == 0:
            continue
        else:
            deli_index = i
            break
    if deli_index != 0:
        for i in range(deli_index, -1, -1):
            if deli_move_remain == cap:
                if deliveries[i] != 0:
                    deli_move_list.append(i + 1)

            if deliveries[i] > deli_move_remain:
                a = deliveries[i] - deli_move_remain
                b = a // cap
                c = a % cap
                for _ in range(b):
                    deli_move_list.append(i + 1)
                if c == 0:
                    deli_move_remain = cap
                else:
                    deli_move_list.append(i + 1)
                    deli_move_remain = cap - c

            elif deliveries[i] == deli_move_remain:
                deli_move_remain = cap

            else:
                deli_move_remain -= deliveries[i]

    for i in range(n - 1, -1, -1):
        if pickups[i] == 0:
            continue
        else:
            pick_index = i
            break
    if pick_index != 0:
        for i in range(pick_index, -1, -1):
            if pick_move_remain == cap:
                if pickups[i] != 0:
                    pick_move_list.append(i + 1)

            if pickups[i] > pick_move_remain:
                a = pickups[i] - pick_move_remain
                b = a // cap
                c = a % cap
                for _ in range(b):
                    pick_move_list.append(i + 1)
                if c == 0:
                    pick_move_remain = cap
                else:
                    pick_move_list.append(i + 1)
                    pick_move_remain = cap - c

            elif pickups[i] == pick_move_remain:
                pick_move_remain = cap

            else:
                pick_move_remain -= pickups[i]

    result = 0
    max_idx = max(len(deli_move_list), len(pick_move_list))
    for i in range(max_idx):
        if len(deli_move_list) > i and len(pick_move_list) > i:
            result += max(deli_move_list[i], pick_move_list[i])
        else:
            if len(deli_move_list) == max_idx:
                result += deli_move_list[i]
            else:
                result += pick_move_list[i]

    return result * 2
  

# 코멘트 : 오랜만에 다시 시작해서 감이 좀 죽은듯. 연습하자.
