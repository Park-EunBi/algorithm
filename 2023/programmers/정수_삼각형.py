def solution(triangle):
    n = len(triangle)
    m = len(triangle[n - 1])

    # 1. dp 정의
    dp = [[0 for _ in range(n)] for _ in range(m)]

    # 2. dp 초기화
    dp[0][0] = triangle[0][0]

    for i in range(1, n):
        dp[i][0] = dp[i - 1][0] + triangle[i][0]
        dp[i][i] = dp[i - 1][i - 1] + triangle[i][i]

    # 3. 점화식
    for i in range(2, n):
        for j in range(1, i):
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1]) + triangle[i][j]

    return max(dp[n - 1])