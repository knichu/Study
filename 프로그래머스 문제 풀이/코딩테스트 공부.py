def solution(alp, cop, problems):
    INF = float('inf')
    min_alp_req = 0
    min_cop_req = 0
    new_problems = []
    for i in problems:
        min_alp_req = max(i[0], min_alp_req)
        min_cop_req = max(i[1], min_cop_req)
        if i[4] < (i[2] + i[3]):
            new_problems.append(i)
    
    alp = min(alp, min_alp_req)
    cop = min(cop, min_cop_req)

    dp = [[INF] * (min_cop_req + 1) for _ in range(min_alp_req + 1)]
    dp[alp][cop] = 0

    for i in range(alp, min_alp_req + 1):
        for j in range(cop, min_cop_req + 1):
            if i < min_alp_req:
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + 1)
            if j < min_cop_req:
                dp[i][j + 1] = min(dp[i][j + 1], dp[i][j] + 1)
            for k in new_problems:
                if k[0] <= i and k[1] <= j:
                    a = min(i + k[2], min_alp_req)
                    b = min(j + k[3], min_cop_req)
                    dp[a][b] = min(dp[a][b], dp[i][j] + k[4])

    return dp[-1][-1]
  
  # 코멘트 : 사고과정 모두 노션에 정리함.
