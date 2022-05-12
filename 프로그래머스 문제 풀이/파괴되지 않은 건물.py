def solution(board, skill):
    
    p = len(board)
    q = len(board[0])
    
    board_state = [[0] * q for i in range(p)]
    
    for k in skill:
        ty, x1, y1, x2, y2, degree = k
        if ty == 1:
            board_state[x1][y1] -= degree
            if y2 + 1 < q:
                board_state[x1][y2 + 1] += degree
            if x2 + 1 < p:
                board_state[x2 + 1][y1] += degree
                if y2 + 1 < q:
                    board_state[x2 + 1][y2 + 1] -= degree

        else: # elif ty == 2:
            board_state[x1][y1] += degree
            if y2 + 1 < q:
                board_state[x1][y2 + 1] -= degree
            if x2 + 1 < p:
                board_state[x2 + 1][y1] -= degree
                if y2 + 1 < q:
                    board_state[x2 + 1][y2 + 1] += degree
    
    for i in range(p - 1):
        for j in range(q):
            board_state[i + 1][j] += board_state[i][j]
        for j in range(q - 1):
            board_state[i][j + 1] += board_state[i][j]
    
    for j in range(q - 1):
        board_state[p - 1][j + 1] += board_state[p - 1][j]
    
    cnt = 0
    for i in range(p):
        for j in range(q):       
            if (board[i][j] + board_state[i][j]) > 0:
                cnt += 1
       
    return cnt


# 예시
board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]
print(solution(board, skill))

board = [[1,2,3],[4,5,6],[7,8,9]]
skill = [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]
print(solution(board, skill))
